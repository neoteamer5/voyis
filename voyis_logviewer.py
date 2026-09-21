#!/usr/bin/env python3
"""
GUI Log Viewer for interleaved Voyis/system logs.

Features:
  * Open multiple log files and combine them into one timeline.
  * Sort by timestamp, output source, level, file, or line.
  * Show/hide records from individual output sources.
  * Multi-select sources: only selected sources are displayed.
  * Search message/source/file with AND / OR logic.
  * Time-range filtering.
  * Double-click a row to see the complete original log line.
  * Export the currently visible rows to CSV.

Search examples:

  warn
      Match lines containing "warn".

  warn or error
      Match lines containing "warn" OR "error".

  warn and error
      Match lines containing BOTH "warn" AND "error".

  camera or timeout or error
      Match lines containing any of the three terms.

Search is case-insensitive.

Supported examples:

[2026-05-27 16:06:03.017] [discovery_headless] [info] message

1779898533954393,SYSLOG_IDENTIFIER=StereoCameraNodeApp,_PID=5718,MESSAGE=[2026-05-27 16:15:33.954] [info] FPS: ...

The application timestamp inside MESSAGE is preferred for journald-style
records, so records from different output sources can be placed on the same
millisecond-resolution timeline.
"""

from __future__ import annotations

import csv
import re
import tkinter as tk
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from tkinter import filedialog, messagebox, ttk


APP_RE = re.compile(
    r"^\[(?P<ts>\d{4}-\d{2}-\d{2} \d\d:\d\d:\d\d(?:[.,]\d{3,6})?)\]"
    r"(?:\s+\[(?P<source>[^\]]+)\])?"
    r"(?:\s+\[(?P<level>[^\]]+)\])?"
    r"\s*(?P<message>.*)$"
)

JOURNAL_RE = re.compile(r"^(?P<epoch>\d{10,20}),(?P<fields>.*)$")

FIELD_RE = re.compile(
    r"(?P<key>[A-Za-z0-9_]+)=(?P<value>.*?)(?=,[A-Za-z0-9_]+=|$)"
)

MESSAGE_TS_RE = re.compile(
    r"^\[(?P<ts>\d{4}-\d{2}-\d{2} \d\d:\d\d:\d\d(?:[.,]\d{3,6})?)\]"
)


@dataclass
class LogRecord:
    timestamp: datetime
    source: str
    level: str
    pid: str
    filename: str
    line_number: int
    message: str
    original: str


def parse_timestamp(s: str) -> datetime | None:
    s = s.replace(",", ".")

    for fmt in ("%Y-%m-%d %H:%M:%S.%f", "%Y-%m-%d %H:%M:%S"):
        try:
            return datetime.strptime(s, fmt)
        except ValueError:
            pass

    return None


def epoch_to_datetime(value: int) -> datetime | None:
    try:
        # Common journald export is microseconds since Unix epoch.
        if value > 10**14:
            return datetime.fromtimestamp(
                value / 1_000_000,
                tz=timezone.utc
            ).replace(tzinfo=None)

        if value > 10**11:
            return datetime.fromtimestamp(
                value / 1_000,
                tz=timezone.utc
            ).replace(tzinfo=None)

        return datetime.fromtimestamp(
            value,
            tz=timezone.utc
        ).replace(tzinfo=None)

    except (ValueError, OSError, OverflowError):
        return None


def parse_line(line: str, filename: str, line_number: int) -> LogRecord:
    original = line.rstrip("\r\n")

    # Normal application log:
    # [timestamp] [source] [level] message
    m = APP_RE.match(original)

    if m:
        ts = parse_timestamp(m.group("ts"))

        if ts:
            return LogRecord(
                ts,
                (m.group("source") or "UNKNOWN").strip(),
                (m.group("level") or "").strip().upper(),
                "",
                filename,
                line_number,
                m.group("message").strip(),
                original,
            )

    # Journald/syslog export:
    # epoch,SYSLOG_IDENTIFIER=...,MESSAGE=[timestamp] [level] ...
    jm = JOURNAL_RE.match(original)

    if jm:
        fields = {}

        for f in FIELD_RE.finditer(jm.group("fields")):
            fields[f.group("key")] = f.group("value")

        message = fields.get("MESSAGE", "").strip()

        source = (
            fields.get("SYSLOG_IDENTIFIER")
            or fields.get("_COMM")
            or "UNKNOWN"
        ).strip()

        pid = fields.get("_PID", "").strip()

        ts = None

        mts = MESSAGE_TS_RE.match(message)

        if mts:
            ts = parse_timestamp(mts.group("ts"))

        if ts is None:
            try:
                ts = epoch_to_datetime(int(jm.group("epoch")))
            except ValueError:
                pass

        if ts:
            # Try to identify [info], [warning], [error], etc.
            am = APP_RE.match(message)
            level = (am.group("level") if am else "") or ""

            return LogRecord(
                ts,
                source,
                level.strip().upper(),
                pid,
                filename,
                line_number,
                message,
                original,
            )

    # Unknown lines remain visible instead of being discarded.
    return LogRecord(
        datetime.min,
        "UNKNOWN",
        "",
        "",
        filename,
        line_number,
        original,
        original,
    )


def read_log(path: Path) -> list[LogRecord]:
    records = []

    with path.open("r", encoding="utf-8", errors="replace") as f:
        for n, line in enumerate(f, 1):
            if line.strip():
                records.append(parse_line(line, path.name, n))

    return records


class LogViewer(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Voyis Combined Log Viewer")
        self.geometry("1550x900")
        self.minsize(1050, 650)

        self.paths: list[Path] = []
        self.records: list[LogRecord] = []
        self.visible_records: list[LogRecord] = []

        # Sources checked in the source list are visible.
        self.source_vars: dict[str, tk.BooleanVar] = {}

        self.search_var = tk.StringVar()
        self.from_var = tk.StringVar()
        self.to_var = tk.StringVar()
        self.status_var = tk.StringVar(
            value="Open one or more log files."
        )

        self.sort_column = "timestamp"
        self.sort_reverse = False

        self.build_ui()

    # ------------------------------------------------------------------
    # UI
    # ------------------------------------------------------------------

    def build_ui(self):
        top = ttk.Frame(self, padding=6)
        top.pack(fill="x")

        ttk.Button(
            top,
            text="Open Log(s)",
            command=self.open_logs
        ).pack(side="left")

        ttk.Button(
            top,
            text="Reload",
            command=self.reload
        ).pack(side="left", padx=5)

        ttk.Button(
            top,
            text="Export CSV",
            command=self.export_csv
        ).pack(side="left")

        ttk.Label(
            top,
            text="   Search:"
        ).pack(side="left")

        search = ttk.Entry(
            top,
            textvariable=self.search_var,
            width=35
        )

        search.pack(side="left", padx=4)

        search.bind(
            "<KeyRelease>",
            lambda e: self.apply_filters()
        )

        ttk.Button(
            top,
            text="Clear Filters",
            command=self.clear_filters
        ).pack(side="left", padx=5)

        # Main split
        main = ttk.Panedwindow(
            self,
            orient="horizontal"
        )

        main.pack(
            fill="both",
            expand=True,
            padx=6,
            pady=(0, 6)
        )

        # Source panel
        source_frame = ttk.Frame(
            main,
            padding=6
        )

        main.add(
            source_frame,
            weight=0
        )

        ttk.Label(
            source_frame,
            text="Output Sources\n(check = show)",
            font=("TkDefaultFont", 10, "bold"),
        ).pack(
            anchor="w",
            pady=(0, 6)
        )

        source_buttons = ttk.Frame(source_frame)
        source_buttons.pack(
            fill="x",
            pady=(0, 5)
        )

        ttk.Button(
            source_buttons,
            text="All",
            command=lambda: self.set_all_sources(True)
        ).pack(side="left")

        ttk.Button(
            source_buttons,
            text="None",
            command=lambda: self.set_all_sources(False)
        ).pack(
            side="left",
            padx=3
        )

        self.source_canvas = tk.Canvas(
            source_frame,
            width=250,
            highlightthickness=0
        )

        source_scroll = ttk.Scrollbar(
            source_frame,
            orient="vertical",
            command=self.source_canvas.yview
        )

        self.source_canvas.configure(
            yscrollcommand=source_scroll.set
        )

        self.source_inner = ttk.Frame(
            self.source_canvas
        )

        self.source_canvas.create_window(
            (0, 0),
            window=self.source_inner,
            anchor="nw"
        )

        self.source_inner.bind(
            "<Configure>",
            lambda e: self.source_canvas.configure(
                scrollregion=self.source_canvas.bbox("all")
            ),
        )

        self.source_canvas.pack(
            side="left",
            fill="both",
            expand=True
        )

        source_scroll.pack(
            side="right",
            fill="y"
        )

        # Right side
        right = ttk.Frame(main)
        main.add(right, weight=1)

        # Time filter
        tf = ttk.Frame(
            right,
            padding=(0, 0, 0, 6)
        )

        tf.pack(fill="x")

        ttk.Label(
            tf,
            text="From:"
        ).pack(side="left")

        ttk.Entry(
            tf,
            textvariable=self.from_var,
            width=22
        ).pack(
            side="left",
            padx=4
        )

        ttk.Label(
            tf,
            text="To:"
        ).pack(
            side="left",
            padx=(8, 0)
        )

        ttk.Entry(
            tf,
            textvariable=self.to_var,
            width=22
        ).pack(
            side="left",
            padx=4
        )

        ttk.Label(
            tf,
            text=" YYYY-MM-DD HH:MM:SS[.mmm]"
        ).pack(side="left")

        ttk.Button(
            tf,
            text="Apply",
            command=self.apply_filters
        ).pack(
            side="left",
            padx=8
        )

        # Table
        table_frame = ttk.Frame(right)
        table_frame.pack(
            fill="both",
            expand=True
        )

        columns = (
            "timestamp",
            "source",
            "level",
            "pid",
            "file",
            "line",
            "message"
        )

        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            selectmode="browse"
        )

        headings = {
            "timestamp": "Timestamp",
            "source": "Output Source",
            "level": "Level",
            "pid": "PID",
            "file": "File",
            "line": "Line",
            "message": "Message",
        }

        widths = {
            "timestamp": 190,
            "source": 200,
            "level": 85,
            "pid": 70,
            "file": 180,
            "line": 65,
            "message": 850,
        }

        for col in columns:
            self.tree.heading(
                col,
                text=headings[col],
                command=lambda c=col: self.sort_by(c),
            )

            self.tree.column(
                col,
                width=widths[col],
                anchor="w"
            )

        ys = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.tree.yview
        )

        xs = ttk.Scrollbar(
            table_frame,
            orient="horizontal",
            command=self.tree.xview
        )

        self.tree.configure(
            yscrollcommand=ys.set,
            xscrollcommand=xs.set
        )

        self.tree.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        ys.grid(
            row=0,
            column=1,
            sticky="ns"
        )

        xs.grid(
            row=1,
            column=0,
            sticky="ew"
        )

        table_frame.rowconfigure(
            0,
            weight=1
        )

        table_frame.columnconfigure(
            0,
            weight=1
        )

        self.tree.bind(
            "<Double-1>",
            self.show_original
        )

        self.tree.bind(
            "<Return>",
            self.show_original
        )

        ttk.Label(
            self,
            textvariable=self.status_var,
            relief="sunken",
            anchor="w",
            padding=4,
        ).pack(
            fill="x",
            side="bottom"
        )

    # ------------------------------------------------------------------
    # Files
    # ------------------------------------------------------------------

    def open_logs(self):
        names = filedialog.askopenfilenames(
            title="Open log files",
            filetypes=[
                ("Log files", "*.log *.txt *.out"),
                ("All files", "*.*"),
            ],
        )

        if names:
            self.paths = [Path(n) for n in names]
            self.load()

    def reload(self):
        if not self.paths:
            messagebox.showinfo(
                "Reload",
                "No log files are loaded."
            )
            return

        self.load()

    def load(self):
        try:
            self.records = []

            for path in self.paths:
                self.records.extend(
                    read_log(path)
                )

            # Initial global chronological order.
            self.records.sort(
                key=lambda r: (
                    r.timestamp,
                    r.filename,
                    r.line_number
                )
            )

            self.rebuild_source_panel()
            self.apply_filters()

            self.status_var.set(
                f"{len(self.records):,} records loaded from "
                f"{len(self.paths)} file(s). "
                f"Visible: {len(self.visible_records):,}"
            )

        except OSError as e:
            messagebox.showerror(
                "Cannot read log",
                str(e)
            )

    # ------------------------------------------------------------------
    # Source show/hide
    # ------------------------------------------------------------------

    def rebuild_source_panel(self):
        for widget in self.source_inner.winfo_children():
            widget.destroy()

        sources = sorted(
            {r.source for r in self.records}
        )

        # Preserve previous selections where possible.
        old = self.source_vars
        self.source_vars = {}

        for source in sources:
            var = tk.BooleanVar(
                value=old.get(
                    source,
                    tk.BooleanVar(value=True)
                ).get()
            )

            self.source_vars[source] = var

            cb = ttk.Checkbutton(
                self.source_inner,
                text=source,
                variable=var,
                command=self.apply_filters,
            )

            cb.pack(
                anchor="w",
                fill="x",
                pady=1
            )

    def set_all_sources(self, value: bool):
        for var in self.source_vars.values():
            var.set(value)

        self.apply_filters()

    # ------------------------------------------------------------------
    # Filters
    # ------------------------------------------------------------------

    def parse_filter_time(self, value: str):
        value = value.strip()

        if not value:
            return None

        for fmt in (
            "%Y-%m-%d %H:%M:%S.%f",
            "%Y-%m-%d %H:%M:%S",
            "%Y-%m-%d",
        ):
            try:
                return datetime.strptime(
                    value,
                    fmt
                )
            except ValueError:
                pass

        raise ValueError(
            f"Invalid time: {value}"
        )

    def matches_search(self, record: LogRecord, search_text: str) -> bool:
        """
        Apply simple AND / OR Boolean search.

        Examples:

            warn
                -> contains "warn"

            warn or error
                -> contains "warn" OR "error"

            warn and error
                -> contains "warn" AND "error"

            camera or timeout or error
                -> contains any term

        Operators are case-insensitive.

        Search is performed against:
            message
            source
            level
            pid
            filename
        """

        search_text = search_text.strip().lower()

        if not search_text:
            return True

        haystack = (
            record.message
            + " "
            + record.source
            + " "
            + record.level
            + " "
            + record.pid
            + " "
            + record.filename
        ).lower()

        # --------------------------------------------------------------
        # OR has lower precedence than AND.
        #
        # Example:
        #
        #     warn or error
        #
        # becomes:
        #
        #     [warn] OR [error]
        #
        # And:
        #
        #     camera and warn or error
        #
        # becomes:
        #
        #     [camera AND warn] OR [error]
        # --------------------------------------------------------------

        or_groups = re.split(
            r"\s+\bor\b\s+",
            search_text,
            flags=re.IGNORECASE
        )

        for group in or_groups:

            and_terms = re.split(
                r"\s+\band\b\s+",
                group,
                flags=re.IGNORECASE
            )

            and_terms = [
                term.strip()
                for term in and_terms
                if term.strip()
            ]

            if and_terms and all(
                term in haystack
                for term in and_terms
            ):
                return True

        return False

    def apply_filters(self):
        if not self.records:
            self.refresh_table([])
            return

        try:
            start = self.parse_filter_time(
                self.from_var.get()
            )

            end = self.parse_filter_time(
                self.to_var.get()
            )

        except ValueError as e:
            self.status_var.set(str(e))
            return

        selected = {
            source
            for source, var in self.source_vars.items()
            if var.get()
        }

        search_text = self.search_var.get()

        result = []

        for r in self.records:

            if r.source not in selected:
                continue

            if start and r.timestamp < start:
                continue

            if end and r.timestamp > end:
                continue

            # Boolean search.
            if search_text and not self.matches_search(
                r,
                search_text
            ):
                continue

            result.append(r)

        self.visible_records = result

        self.refresh_table(result)

        self.status_var.set(
            f"Loaded: {len(self.records):,} | "
            f"Visible: {len(result):,} | "
            f"Sources shown: "
            f"{len(selected)}/{len(self.source_vars)}"
        )

    def clear_filters(self):
        self.search_var.set("")
        self.from_var.set("")
        self.to_var.set("")

        self.set_all_sources(True)

    # ------------------------------------------------------------------
    # Sorting
    # ------------------------------------------------------------------

    def sort_by(self, column):
        if self.sort_column == column:
            self.sort_reverse = not self.sort_reverse
        else:
            self.sort_column = column
            self.sort_reverse = False

        key_functions = {
            "timestamp": lambda r: r.timestamp,
            "source": lambda r: r.source.lower(),
            "level": lambda r: r.level.lower(),
            "pid": lambda r: r.pid,
            "file": lambda r: r.filename.lower(),
            "line": lambda r: r.line_number,
            "message": lambda r: r.message.lower(),
        }

        self.visible_records.sort(
            key=key_functions[column],
            reverse=self.sort_reverse,
        )

        self.refresh_table(
            self.visible_records
        )

    # ------------------------------------------------------------------
    # Table
    # ------------------------------------------------------------------

    def refresh_table(self, records):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for index, r in enumerate(records):
            self.tree.insert(
                "",
                "end",
                iid=str(index),
                values=(
                    r.timestamp.strftime(
                        "%Y-%m-%d %H:%M:%S.%f"
                    )[:-3]
                    if r.timestamp != datetime.min
                    else "UNKNOWN",
                    r.source,
                    r.level,
                    r.pid,
                    r.filename,
                    r.line_number,
                    r.message,
                ),
            )

    def show_original(self, event=None):
        selected = self.tree.selection()

        if not selected:
            return

        index = int(selected[0])

        if index >= len(self.visible_records):
            return

        r = self.visible_records[index]

        win = tk.Toplevel(self)

        win.title(
            f"{r.source} - "
            f"{r.filename}:{r.line_number}"
        )

        win.geometry("1100x500")

        text = tk.Text(
            win,
            wrap="none"
        )

        ys = ttk.Scrollbar(
            win,
            orient="vertical",
            command=text.yview
        )

        xs = ttk.Scrollbar(
            win,
            orient="horizontal",
            command=text.xview
        )

        text.configure(
            yscrollcommand=ys.set,
            xscrollcommand=xs.set
        )

        text.insert(
            "1.0",
            r.original
        )

        text.configure(
            state="disabled"
        )

        text.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        ys.grid(
            row=0,
            column=1,
            sticky="ns"
        )

        xs.grid(
            row=1,
            column=0,
            sticky="ew"
        )

        win.rowconfigure(
            0,
            weight=1
        )

        win.columnconfigure(
            0,
            weight=1
        )

    # ------------------------------------------------------------------
    # CSV
    # ------------------------------------------------------------------

    def export_csv(self):
        if not self.visible_records:
            messagebox.showinfo(
                "Export CSV",
                "There are no visible records."
            )
            return

        filename = filedialog.asksaveasfilename(
            title="Export visible records",
            defaultextension=".csv",
            filetypes=[
                ("CSV files", "*.csv"),
                ("All files", "*.*"),
            ],
        )

        if not filename:
            return

        try:
            with open(
                filename,
                "w",
                newline="",
                encoding="utf-8"
            ) as f:

                writer = csv.writer(f)

                writer.writerow(
                    [
                        "timestamp",
                        "source",
                        "level",
                        "pid",
                        "file",
                        "line",
                        "message",
                        "original",
                    ]
                )

                for r in self.visible_records:
                    writer.writerow(
                        [
                            r.timestamp.strftime(
                                "%Y-%m-%d %H:%M:%S.%f"
                            )[:-3]
                            if r.timestamp != datetime.min
                            else "",
                            r.source,
                            r.level,
                            r.pid,
                            r.filename,
                            r.line_number,
                            r.message,
                            r.original,
                        ]
                    )

            messagebox.showinfo(
                "Export CSV",
                f"Exported "
                f"{len(self.visible_records):,} records.",
            )

        except OSError as e:
            messagebox.showerror(
                "Export failed",
                str(e)
            )


if __name__ == "__main__":
    LogViewer().mainloop()

