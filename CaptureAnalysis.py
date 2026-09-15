import re
import sys
from dataclasses import dataclass


@dataclass
class CaptureResult:
    number: int
    start_time: str
    expected_images: int
    deadline_seconds: float
    actual_images: int | None = None
    duration_seconds: float | None = None
    led_failure: bool = False
    api_timeout: bool = False
    result: str = "INCOMPLETE"
    reason: str = ""


def parse_capture_sessions(log_text):
    # Example:
    # [2026-05-27 17:19:29.161] [discovery_headless] [info]
    # Capturing 10 images at 1 Hz save rate (deadline: 15 s)...

    start_pattern = re.compile(
        r"\[(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}\.\d{3})\].*?"
        r"Capturing\s+(\d+)\s+images\s+at\s+"
        r"([0-9]+(?:\.[0-9]+)?)\s+Hz\s+save\s+rate\s+"
        r"\(deadline:\s*([0-9]+(?:\.[0-9]+)?)\s*s\)",
        re.IGNORECASE
    )

    # Example:
    # [2026-05-27 17:19:39.544] ...
    # Capture Session: 10 images in 10.38 s

    complete_pattern = re.compile(
        r"\[(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}\.\d{3})\].*?"
        r"Capture Session:\s+(\d+)\s+images\s+in\s+"
        r"([0-9]+(?:\.[0-9]+)?)\s+s",
        re.IGNORECASE
    )

    led_pattern = re.compile(
        r"\[.*?\].*?Failed to turn off LED",
        re.IGNORECASE
    )

    timeout_pattern = re.compile(
        r"\[.*?\].*?Request timeout in the API instance",
        re.IGNORECASE
    )

    starts = list(start_pattern.finditer(log_text))
    completions = list(complete_pattern.finditer(log_text))
    led_failures = list(led_pattern.finditer(log_text))
    api_timeouts = list(timeout_pattern.finditer(log_text))

    results = []

    completion_index = 0

    for number, start in enumerate(starts, start=1):

        result = CaptureResult(
            number=number,
            start_time=start.group(1),
            expected_images=int(start.group(2)),
            deadline_seconds=float(start.group(4)),
        )

        # Find the first completion after this capture started.
        completion = None

        while completion_index < len(completions):

            candidate = completions[completion_index]

            if candidate.start() > start.end():
                completion = candidate
                completion_index += 1
                break

            completion_index += 1

        # No completion record.
        if completion is None:

            result.result = "INCOMPLETE"

            result.reason = (
                "Capture started, but no corresponding "
                "'Capture Session' completion record was found."
            )

            results.append(result)
            continue

        result.actual_images = int(completion.group(2))
        result.duration_seconds = float(completion.group(3))

        # Look for errors between capture start and completion.
        for match in led_failures:

            if start.end() <= match.start() <= completion.start():
                result.led_failure = True

        for match in api_timeouts:

            if start.end() <= match.start() <= completion.start():
                result.api_timeout = True

        failures = []

        if result.actual_images != result.expected_images:

            failures.append(
                f"expected {result.expected_images} images, "
                f"observed {result.actual_images}"
            )

        if result.duration_seconds > result.deadline_seconds:

            failures.append(
                f"duration {result.duration_seconds:.2f}s "
                f"exceeded deadline {result.deadline_seconds:.2f}s"
            )

        if result.api_timeout:
            failures.append("API request timeout detected")

        if result.led_failure:
            failures.append("LED shutdown failure detected")

        if failures:

            result.result = "FAIL"
            result.reason = "; ".join(failures)

        else:

            result.result = "PASS"
            result.reason = (
                f"{result.actual_images} images captured in "
                f"{result.duration_seconds:.2f}s"
            )

        results.append(result)

    return results


def generate_report(results):

    lines = []

    lines.append("### Capture Result Summary")
    lines.append("")

    lines.append(
        "| Capture | Start Time | Expected | Observed | "
        "Duration | Result |"
    )

    lines.append(
        "|---:|---|---:|---:|---:|:---:|"
    )

    for result in results:

        observed = (
            str(result.actual_images)
            if result.actual_images is not None
            else "-"
        )

        duration = (
            f"{result.duration_seconds:.2f} s"
            if result.duration_seconds is not None
            else "-"
        )

        status = {
            "PASS": "✅ PASS",
            "FAIL": "❌ FAIL",
            "INCOMPLETE": "⚠️ INCOMPLETE",
        }[result.result]

        lines.append(
            f"| #{result.number} "
            f"| {result.start_time} "
            f"| {result.expected_images} "
            f"| {observed} "
            f"| {duration} "
            f"| {status} |"
        )

    lines.append("")

    overall_pass = all(
        result.result == "PASS"
        for result in results
    )

    lines.append(
        "**Overall Verdict: "
        + ("✅ PASS" if overall_pass else "❌ FAIL")
        + "**"
    )

    lines.append("")
    lines.append("### Failure / Incomplete Analysis")
    lines.append("")

    for result in results:

        if result.result == "PASS":
            continue

        lines.append(
            f"**Capture #{result.number} — {result.result}**"
        )

        lines.append("")

        lines.append(
            f"- Start time: `{result.start_time}`"
        )

        lines.append(
            f"- Expected images: `{result.expected_images}`"
        )

        if result.actual_images is not None:

            lines.append(
                f"- Observed images: `{result.actual_images}`"
            )

        if result.duration_seconds is not None:

            lines.append(
                f"- Duration: `{result.duration_seconds:.2f}s`"
            )

        lines.append(
            f"- Determination: {result.reason}"
        )

        lines.append("")

    return "\n".join(lines)


def main():

    if len(sys.argv) != 2:

        print(
            f"Usage: python3 {sys.argv[0]} "
            "<discovery_headless.log>"
        )

        sys.exit(1)

    log_file = sys.argv[1]

    try:

        with open(
            log_file,
            "r",
            encoding="utf-8"
        ) as file:

            log_text = file.read()

    except OSError as error:

        print(f"Error reading log file: {error}")
        sys.exit(1)

    results = parse_capture_sessions(log_text)

    if not results:

        print(
            "No capture sessions found in "
            f"{log_file}."
        )

        sys.exit(1)

    report = generate_report(results)

    print(report)


if __name__ == "__main__":
    main()