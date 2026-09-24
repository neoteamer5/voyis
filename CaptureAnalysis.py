#!/usr/bin/env python3

"""
Capture log analysis for Voyis embedded-system validation.

The analyzer evaluates:
    1. Application-level image count and capture deadline.
    2. System-level 60-second power-on requirement.
    3. Raw and processed image saving evidence.
    4. Stereo left/right image evidence.
    5. LED and API errors during capture.

Usage:
    python3 CaptureAnalysis.py application_runtime.log

    python3 CaptureAnalysis.py application_runtime.log voyis_capture_report.md
"""

import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


EXPECTED_STEREO_PAIRS = 10
MAX_POWER_ON_TIME_SECONDS = 60.0


TIMESTAMP_RE = re.compile(
    r"\[(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}\.\d{3})\]"
)

CAPTURE_START_RE = re.compile(
    r"Capturing\s+(\d+)\s+images\s+at\s+"
    r"([0-9]+(?:\.[0-9]+)?)\s+Hz\s+save\s+rate\s+"
    r"\(deadline:\s*([0-9]+(?:\.[0-9]+)?)\s*s\)",
    re.IGNORECASE,
)

CAPTURE_COMPLETE_RE = re.compile(
    r"Capture Session:\s+(\d+)\s+images\s+in\s+"
    r"([0-9]+(?:\.[0-9]+)?)\s+s",
    re.IGNORECASE,
)
CYCLE_START_RE = re.compile(
    r"discovery_headless\s+version",
    re.IGNORECASE,
)

CYCLE_COMPLETE_RE = re.compile(
    "Idling until power cycle.",
    re.IGNORECASE,
)

DEVICE_DETECTED_RE = re.compile(
    r"Device detected:.*?\(stereo\)",
    re.IGNORECASE,
)

SAVING_ENABLED_RE = re.compile(
    r"Device-side saving enabled:\s*"
    r"raw=(true|false),\s*processed=(true|false)",
    re.IGNORECASE,
)

RAW_WRITE_RE = re.compile(
    r"/Raw_[^/\s]+/(Left|Right)/",
    re.IGNORECASE,
)

PROCESSED_WRITE_RE = re.compile(
    r"/Processed_[^/\s]+/(Left|Right)/",
    re.IGNORECASE,
)

LED_FAILURE_RE = re.compile(
    r"Failed to turn off LED",
    re.IGNORECASE,
)

API_TIMEOUT_RE = re.compile(
    r"Request timeout in the API instance",
    re.IGNORECASE,
)


@dataclass
class CaptureResult:
    """Store the validation results for one capture session."""

    number: int
    start_time: str
    expected_images: int
    application_deadline_seconds: float

    actual_images: int | None = None
    duration_seconds: float | None = None

    device_detected_time: str | None = None
    power_on_to_completion_seconds: float | None = None

    raw_enabled: bool = False
    processed_enabled: bool = False

    raw_left_files: int = 0
    raw_right_files: int = 0
    processed_left_files: int = 0
    processed_right_files: int = 0

    led_failure: bool = False
    api_timeout: bool = False

    result: str = "INCOMPLETE"
    reason: str = ""


def parse_timestamp(line: str) -> datetime | None:
    """
    Extract the timestamp from a log line.

    Args:
        line: Raw log line.

    Returns:
        Parsed datetime, or None if no timestamp is present.
    """
    match = TIMESTAMP_RE.search(line)

    if not match:
        return None

    return datetime.strptime(
        match.group(1),
        "%Y-%m-%d %H:%M:%S.%f",
    )


def calculate_elapsed_seconds(
    start: datetime,
    end: datetime,
) -> float:
    """
    Calculate elapsed time between two timestamps.

    Args:
        start: Start timestamp.
        end: End timestamp.

    Returns:
        Elapsed time in seconds.
    """
    return (end - start).total_seconds()


def create_capture(
    number: int,
    timestamp: datetime,
    expected_images: int,
    deadline: float,
) -> CaptureResult:
    """
    Create a new capture result.

    Args:
        number: Capture sequence number.
        timestamp: Capture start timestamp.
        expected_images: Number of images expected by application.
        deadline: Application capture deadline.

    Returns:
        New CaptureResult instance.
    """
    return CaptureResult(
        number=number,
        start_time=timestamp.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3],
        expected_images=expected_images,
        application_deadline_seconds=deadline,
    )


def classify_line(
    line: str,
    timestamp: datetime | None,
    current: CaptureResult | None,
) -> None:
    """
    Apply relevant log information to the active capture session.

    Args:
        line: Raw log line.
        timestamp: Parsed log timestamp.
        current: Active capture session.
    """
    if current is None:
        return
    if "Device-side saving enabled" in line:
        print("MATCH TEST:", SAVING_ENABLED_RE.search(line))
        
    match = SAVING_ENABLED_RE.search(line)

    if match:
        current.raw_enabled = match.group(1).lower() == "true"
        current.processed_enabled = match.group(2).lower() == "true"

    if RAW_WRITE_RE.search(line):
        current.raw_left_files += int(
            bool(re.search(r"/Left/", line, re.IGNORECASE))
        )
        current.raw_right_files += int(
            bool(re.search(r"/Right/", line, re.IGNORECASE))
        )

    if PROCESSED_WRITE_RE.search(line):
        current.processed_left_files += int(
            bool(re.search(r"/Left/", line, re.IGNORECASE))
        )
        current.processed_right_files += int(
            bool(re.search(r"/Right/", line, re.IGNORECASE))
        )

    if LED_FAILURE_RE.search(line):
        current.led_failure = True

    if API_TIMEOUT_RE.search(line):
        current.api_timeout = True


def finalize_capture(capture: CaptureResult) -> None:
    """
    Determine the final verdict for a completed capture.

    Args:
        capture: Capture result to finalize.
    """
    failures = []

    if capture.actual_images is None:
        capture.result = "INCOMPLETE"
        capture.reason = "No capture completion record."
        return

    if capture.actual_images != capture.expected_images:
        failures.append(
            f"expected {capture.expected_images} images, "
            f"observed {capture.actual_images}"
        )

    if (
        capture.duration_seconds is not None
        and capture.duration_seconds
        > capture.application_deadline_seconds
    ):
        failures.append(
            f"capture duration {capture.duration_seconds:.2f}s "
            f"exceeded application deadline "
            f"{capture.application_deadline_seconds:.2f}s"
        )

    if (
        capture.power_on_to_completion_seconds is not None
        and capture.power_on_to_completion_seconds
        > MAX_POWER_ON_TIME_SECONDS
    ):
        failures.append(
            f"power-on to completion "
            f"{capture.power_on_to_completion_seconds:.2f}s "
            f"exceeded {MAX_POWER_ON_TIME_SECONDS:.0f}s system limit"
        )

    if capture.led_failure:
        failures.append("LED disable failure detected")

    if capture.api_timeout:
        failures.append("API timeout detected")

    if failures:
        capture.result = "FAIL"
        capture.reason = "; ".join(failures)
    else:
        capture.result = "PASS"
        capture.reason = "All observed application checks passed."


def analyze_log(log_path: Path) -> list[CaptureResult]:
    """
    Analyze the application runtime log.

    One CaptureResult represents one complete power-cycle run.

    Cycle:
        discovery_headless version
            ->
        Capturing N images...
            ->
        Capture Session: N images in X s
            ->
        Idling until power cycle.

    Returns:
        List of capture validation results.
    """
    captures: list[CaptureResult] = []

    current: CaptureResult | None = None

    capture_number = 0
    last_device_detected: datetime | None = None

    with log_path.open(
        "r",
        encoding="utf-8",
        errors="replace",
    ) as log_file:

        for line in log_file:
            timestamp = parse_timestamp(line)

            if timestamp is None:
                continue

            # ---------------------------------------------------------
            # Device detected
            # ---------------------------------------------------------
            if DEVICE_DETECTED_RE.search(line):
                last_device_detected = timestamp

            # ---------------------------------------------------------
            # Start of a NEW full cycle
            # ---------------------------------------------------------
            cycle_start_match = CYCLE_START_RE.search(line)
            if cycle_start_match:

                # Previous cycle did not reach:
                # "Idling until power cycle."
                if current is not None:
                    finalize_capture(current)
                    captures.append(current)

                capture_number += 1

                # We don't have capture information yet.
                current = create_capture(
                    number=capture_number,
                    timestamp=timestamp,
                    expected_images=0,
                    deadline=0,
                )

                continue

            if current is None:
                continue

            # ---------------------------------------------------------
            # Classify all lines belonging to this cycle.
            #
            # This allows lines such as:
            #   Device-side saving enabled...
            #   Camera settings confirmed...
            #   LED disabled.
            #   Boot time recorded...
            #
            # to be processed before capture completion.
            # ---------------------------------------------------------
            classify_line(line, timestamp, current)

            # ---------------------------------------------------------
            # Capture START
            # ---------------------------------------------------------
            start_match = CAPTURE_START_RE.search(line)

            if start_match:
                current.expected_images = int(start_match.group(1))
                current.save_rate_hz = float(start_match.group(2))
                current.deadline_seconds = float(start_match.group(3))

                current.device_detected_time = (
                    last_device_detected.strftime(
                        "%Y-%m-%d %H:%M:%S.%f"
                    )[:-3]
                    if last_device_detected
                    else None
                )

                continue

            # ---------------------------------------------------------
            # Capture COMPLETE
            #
            # This does NOT finalize the full cycle.
            # ---------------------------------------------------------
            complete_match = CAPTURE_COMPLETE_RE.search(line)

            if complete_match:
                current.actual_images = int(
                    complete_match.group(1)
                )

                current.duration_seconds = float(
                    complete_match.group(2)
                )

                continue

            # ---------------------------------------------------------
            # FULL CYCLE COMPLETE
            # ---------------------------------------------------------
            if CYCLE_COMPLETE_RE.search(line):

                if last_device_detected is not None:
                    current.power_on_to_completion_seconds = (
                        calculate_elapsed_seconds(
                            last_device_detected,
                            timestamp,
                        )
                    )

                finalize_capture(current)

                captures.append(current)

                current = None

    # -------------------------------------------------------------
    # Log ended before "Idling until power cycle."
    # Therefore this is an incomplete cycle.
    # -------------------------------------------------------------
    if current is not None:
        finalize_capture(current)
        captures.append(current)

    return captures

def verification_status(
    actual_left: int,
    actual_right: int,
    expected: int,
) -> str:
    """
    Determine whether left/right file evidence verifies stereo pairs.

    Args:
        actual_left: Number of left images observed.
        actual_right: Number of right images observed.
        expected: Required stereo-pair count.

    Returns:
        PASS, FAIL, or NOT VERIFIED.
    """
    if actual_left == 0 and actual_right == 0:
        return "NOT VERIFIED"

    if actual_left >= expected and actual_right >= expected:
        return "PASS"

    return "FAIL"


def print_console_summary(captures: list[CaptureResult]) -> None:
    """
    Print a readable summary of capture analysis to the console.

    Args:
        captures: Capture validation results.
    """
    print()
    print("Capture Analysis")
    print("================")

    for capture in captures:
        if capture.actual_images is None:
            print(
                f"Capture #{capture.number}: "
                f"{capture.result:<10} "
                f"no completion record"
            )
            continue

        print(
            f"Capture #{capture.number}: "
            f"{capture.result:<10} "
            f"{capture.actual_images}/{capture.expected_images} images, "
            f"{capture.duration_seconds:.2f}s"
        )

        if capture.power_on_to_completion_seconds is not None:
            print(
                f"  60s system timing: "
                f"{capture.power_on_to_completion_seconds:.2f}s"
            )

    passed = sum(c.result == "PASS" for c in captures)
    failed = sum(c.result == "FAIL" for c in captures)
    incomplete = sum(c.result == "INCOMPLETE" for c in captures)

    overall = "PASS"

    if failed:
        overall = "FAIL"
    elif incomplete:
        overall = "INCOMPLETE"

    print()
    print(f"Overall: {overall}")
    print(f"Sessions: {len(captures)}")
    print(f"PASS: {passed}")
    print(f"FAIL: {failed}")
    print(f"INCOMPLETE: {incomplete}")


def markdown_status(value: str) -> str:
    """
    Format a validation status for Markdown output.

    Args:
        value: Status string.

    Returns:
        Formatted Markdown status.
    """
    return f"**{value}**"


def build_markdown_report(
    captures: list[CaptureResult],
    log_path: Path,
) -> str:
    """
    Build the detailed Markdown validation report.

    Args:
        captures: Capture validation results.
        log_path: Input log path.

    Returns:
        Markdown report text.
    """
    passed = sum(c.result == "PASS" for c in captures)
    failed = sum(c.result == "FAIL" for c in captures)
    incomplete = sum(c.result == "INCOMPLETE" for c in captures)

    overall = "PASS"

    if failed:
        overall = "FAIL"
    elif incomplete:
        overall = "INCOMPLETE"

    report = []

    report.append("# Capture Analysis Report\n")
    report.append(f"**Input log:** `{log_path}`\n")
    report.append(f"**Overall result:** {markdown_status(overall)}\n")

    report.append("## Requirements\n")
    report.append(
        f"- Expected stereo pairs: **{EXPECTED_STEREO_PAIRS}**"
    )
    report.append(
        f"- Maximum power-on to completion time: "
        f"**{MAX_POWER_ON_TIME_SECONDS:.0f} s**"
    )
    report.append(
        "- Application capture deadline is evaluated separately "
        "from the 60-second system requirement."
    )
    report.append(
        "- `Device detected` is used as the observable power-on "
        "reference because an explicit electrical power-on timestamp "
        "is not present in the application log."
    )

    report.append("\n## Summary\n")
    report.append(
        "| Capture | Result | Images | Duration | "
        "Power-on → Completion |"
    )
    report.append("|---:|---|---:|---:|---:|")

    for capture in captures:
        images = (
            f"{capture.actual_images}/{capture.expected_images}"
            if capture.actual_images is not None
            else "N/A"
        )

        duration = (
            f"{capture.duration_seconds:.2f}s"
            if capture.duration_seconds is not None
            else "N/A"
        )

        power_time = (
            f"{capture.power_on_to_completion_seconds:.2f}s"
            if capture.power_on_to_completion_seconds is not None
            else "N/A"
        )

        report.append(
            f"| {capture.number} | {capture.result} | "
            f"{images} | {duration} | {power_time} |"
        )

    for capture in captures:
        report.append(f"\n## Capture #{capture.number}\n")

        report.append(
            f"**Start time:** `{capture.start_time}`"
        )

        if capture.device_detected_time:
            report.append(
                f"\n**Device detected:** "
                f"`{capture.device_detected_time}`"
            )

        report.append("\n### Application-Level Validation\n")

        if capture.actual_images is None:
            image_status = "INCOMPLETE"
        elif capture.actual_images >= capture.expected_images:
            image_status = "PASS"
        else:
            image_status = "FAIL"

        report.append(
            f"- Image count: "
            f"{markdown_status(image_status)}"
        )

        if capture.actual_images is not None:
            report.append(
                f"  - Expected: {capture.expected_images}"
            )
            report.append(
                f"  - Observed: {capture.actual_images}"
            )

        deadline_status = "NOT VERIFIED"

        if capture.duration_seconds is not None:
            deadline_status = (
                "PASS"
                if capture.duration_seconds
                <= capture.application_deadline_seconds
                else "FAIL"
            )

        report.append(
            f"- Application deadline "
            f"({capture.application_deadline_seconds:.0f}s): "
            f"{markdown_status(deadline_status)}"
        )

        if capture.duration_seconds is not None:
            report.append(
                f"  - Observed duration: "
                f"{capture.duration_seconds:.2f}s"
            )

        report.append("\n### System-Level Validation\n")

        if capture.power_on_to_completion_seconds is None:
            system_status = "NOT VERIFIED"
        else:
            system_status = (
                "PASS"
                if capture.power_on_to_completion_seconds
                <= MAX_POWER_ON_TIME_SECONDS
                else "FAIL"
            )

        report.append(
            f"- 60-second requirement: "
            f"{markdown_status(system_status)}"
        )

        if capture.power_on_to_completion_seconds is not None:
            report.append(
                f"  - Device detection → completion: "
                f"{capture.power_on_to_completion_seconds:.2f}s"
            )

        report.append(
            "\n> Note: the log does not contain an explicit electrical "
            "power-on timestamp. Device detection is therefore used "
            "as an observable proxy."
        )

        report.append("\n### Raw Image Validation\n")

        raw_status = verification_status(
            capture.raw_left_files,
            capture.raw_right_files,
            EXPECTED_STEREO_PAIRS,
        )

        report.append(
            f"- Raw saving enabled: "
            f"{markdown_status('PASS' if capture.raw_enabled else 'FAIL')}"
        )

        report.append(
            f"- Raw Left files observed: "
            f"{capture.raw_left_files}"
        )

        report.append(
            f"- Raw Right files observed: "
            f"{capture.raw_right_files}"
        )

        report.append(
            f"- Raw stereo-pair evidence: "
            f"{markdown_status(raw_status)}"
        )

        report.append("\n### Processed Image Validation\n")

        processed_status = verification_status(
            capture.processed_left_files,
            capture.processed_right_files,
            EXPECTED_STEREO_PAIRS,
        )

        report.append(
            f"- Processed saving enabled: "
            f"{markdown_status('PASS' if capture.processed_enabled else 'FAIL')}"
        )

        report.append(
            f"- Processed Left files observed: "
            f"{capture.processed_left_files}"
        )

        report.append(
            f"- Processed Right files observed: "
            f"{capture.processed_right_files}"
        )

        report.append(
            f"- Processed stereo-pair evidence: "
            f"{markdown_status(processed_status)}"
        )

        report.append("\n### Error Checks\n")

        report.append(
            f"- LED failure: "
            f"{markdown_status('FAIL' if capture.led_failure else 'PASS')}"
        )

        report.append(
            f"- API timeout: "
            f"{markdown_status('FAIL' if capture.api_timeout else 'PASS')}"
        )

        report.append("\n### Capture Verdict\n")

        report.append(
            f"**Result:** {markdown_status(capture.result)}"
        )

        if capture.reason:
            report.append(
                f"\n**Reason:** {capture.reason}"
            )

        if (
            raw_status == "NOT VERIFIED"
            or processed_status == "NOT VERIFIED"
        ):
            report.append(
                "\n**Evidence limitation:** The application log does not "
                "provide enough correlated file-write evidence to prove "
                "the complete raw/processed stereo-pair requirement for "
                "this capture."
            )

    report.append("\n## Overall Assessment\n")

    report.append(
        f"- PASS sessions: {passed}"
    )
    report.append(
        f"- FAIL sessions: {failed}"
    )
    report.append(
        f"- INCOMPLETE sessions: {incomplete}"
    )
    report.append(
        f"- Overall result: **{overall}**"
    )

    return "\n".join(report) + "\n"


def save_markdown_report(
    report: str,
    output_path: Path,
) -> None:
    """
    Save the Markdown report to disk.

    Args:
        report: Markdown report contents.
        output_path: Destination file.
    """
    output_path.write_text(
        report,
        encoding="utf-8",
    )


def main() -> int:
    """
    Run capture analysis from the command line.

    Returns:
        Process exit code.
    """
    if len(sys.argv) < 2:
        print(
            "Usage: python3 CaptureAnalysis.py "
            "<application_runtime.log> "
            "[output.md]"
        )
        log_path = Path("application_runtime.log")
    else:
        log_path = Path(sys.argv[1])

    if not log_path.is_file():
        print(f"Error: log file not found: {log_path}")
        return 1

    output_path = (
        Path(sys.argv[2])
        if len(sys.argv) >= 3
        else Path("capture_analysis.md")
    )

    captures = analyze_log(log_path)

    print_console_summary(captures)

    report = build_markdown_report(
        captures,
        log_path,
    )

    save_markdown_report(
        report,
        output_path,
    )

    print()
    print(f"Detailed report: {output_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())