#!/usr/bin/env python3

import argparse
import json
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path


# Test requirements / thresholds.
# These should eventually come from a configuration file or
# product requirements rather than being hard-coded.
SYNC_LIMIT_US = 1000
NVME_WARNING_TEMP_C = 52.0
NVME_CRITICAL_TEMP_C = 54.0
CPU_CRITICAL_TEMP_C = 96.0
GPU_CRITICAL_TEMP_C = 97.0


@dataclass
class TestResult:
    test_id: str
    description: str
    status: str
    details: str


class LogAnalyzer:
    def __init__(self, log_text: str):
        self.log_text = log_text
        self.results = []

        self.sync_errors_us = []
        self.fps_values = []

        self.raw_left = False
        self.raw_right = False
        self.processed_left = False
        self.processed_right = False

        self.cpu_loads = []
        self.gpu_loads = []
        self.memory_usage = []

        self.nvme_temps = []
        self.cpu_temps = []
        self.gpu_temps = []

        self.time_sync_found = False
        self.time_sync_offset = None

    def analyze(self):
        self.parse_camera_sync()
        self.parse_fps()
        self.parse_image_storage()
        self.parse_system_status()
        self.parse_time_sync()

        self.evaluate_tests()

        return self.results

    # ---------------------------------------------------------
    # Parsing
    # ---------------------------------------------------------

    def parse_camera_sync(self):
        pattern = re.compile(
            r"ImageMatching:.*?diff=(\d+)us",
            re.IGNORECASE
        )

        self.sync_errors_us = [
            int(match.group(1))
            for match in pattern.finditer(self.log_text)
        ]

    def parse_fps(self):
        pattern = re.compile(
            r"FPS:\s+Video\(\s*"
            r"([0-9]+(?:\.[0-9]+)?)\s*,\s*"
            r"\+([0-9]+(?:\.[0-9]+)?)ms\)",
            re.IGNORECASE
        )

        self.fps_values = []
        self.video_latency_ms = []

        for match in pattern.finditer(self.log_text):
            fps = float(match.group(1))
            latency = float(match.group(2))

            self.fps_values.append(fps)
            self.video_latency_ms.append(latency)

    def parse_image_storage(self):
        text = self.log_text.lower()

        self.raw_left = (
            "raw left" in text
            or re.search(r"raw.*left.*\.tif", text) is not None
        )

        self.raw_right = (
            "raw right" in text
            or re.search(r"raw.*right.*\.tif", text) is not None
        )

        self.processed_left = (
            "processed left" in text
            or re.search(r"processed.*left.*", text) is not None
        )

        self.processed_right = (
            "processed right" in text
            or re.search(r"processed.*right.*", text) is not None
        )

    def parse_system_status(self):
        # ------------------------------------------------------------------
        # Resource utilization
        # Example:
        # CPU Load: 208%, GPU Load: 47%, Mem Usage: 32%,
        # Disk Usage: 1%, Network Usage: 0Mbps
        # ------------------------------------------------------------------
        resource_pattern = re.compile(
            r"CPU Load:\s*([0-9]+(?:\.[0-9]+)?)%\s*,\s*"
            r"GPU Load:\s*([0-9]+(?:\.[0-9]+)?)%\s*,\s*"
            r"Mem Usage:\s*([0-9]+(?:\.[0-9]+)?)%",
            re.IGNORECASE
        )

        for match in resource_pattern.finditer(self.log_text):
            self.cpu_loads.append(float(match.group(1)))
            self.gpu_loads.append(float(match.group(2)))
            self.memory_usage.append(float(match.group(3)))

        # ------------------------------------------------------------------
        # NVMe temperature
        # Example:
        # Warning ... Threshold: 52 Celsius,
        # Critical ... Threshold: 54 Celsius,
        # Temperature: 26 Celsius
        #
        # Capture only the actual NVMe temperature, not the thresholds.
        # ------------------------------------------------------------------
        nvme_pattern = re.compile(
            r"NVME Disk Temperature\(s\):.*?"
            r"Temperature:\s*([0-9]+(?:\.[0-9]+)?)\s*Celsius",
            re.IGNORECASE
        )

        for match in nvme_pattern.finditer(self.log_text):
            self.nvme_temps.append(float(match.group(1)))

        # ------------------------------------------------------------------
        # CPU and GPU temperatures
        # Example:
        # Temperature Updates:
        # [CPU-therm: 31.5 C] [GPU-therm: 29 C]
        # ------------------------------------------------------------------
        temperature_pattern = re.compile(
            r"Temperature Updates:.*?"
            r"\[CPU-therm:\s*([0-9]+(?:\.[0-9]+)?)\s*C\].*?"
            r"\[GPU-therm:\s*([0-9]+(?:\.[0-9]+)?)\s*C\]",
            re.IGNORECASE
        )

        for match in temperature_pattern.finditer(self.log_text):
            self.cpu_temps.append(float(match.group(1)))
            self.gpu_temps.append(float(match.group(2)))
            
    def parse_time_sync(self):
        # Example:
        # RMS offset: 0.000000000 seconds
        pattern = re.compile(
            r"RMS offset:\s*([-+]?[0-9]*\.?[0-9]+)\s*seconds",
            re.IGNORECASE
        )

        match = pattern.search(self.log_text)

        if match:
            self.time_sync_found = True
            self.time_sync_offset = float(match.group(1))

    # ---------------------------------------------------------
    # Test evaluation
    # ---------------------------------------------------------

    def evaluate_tests(self):

        # -----------------------------------------------------
        # CAM-SYNC-001
        # -----------------------------------------------------

        if not self.sync_errors_us:
            self.results.append(
                TestResult(
                    "CAM-SYNC-001",
                    "Stereo camera synchronization",
                    "NOT_RUN",
                    "No ImageMatching synchronization data found."
                )
            )
        else:
            max_error = max(self.sync_errors_us)

            if max_error <= SYNC_LIMIT_US:
                status = "PASS"
                details = (
                    f"Maximum synchronization error = "
                    f"{max_error} us, limit = {SYNC_LIMIT_US} us."
                )
            else:
                status = "FAIL"
                details = (
                    f"Synchronization error exceeded limit: "
                    f"maximum = {max_error} us, "
                    f"limit = {SYNC_LIMIT_US} us."
                )

            self.results.append(
                TestResult(
                    "CAM-SYNC-001",
                    "Stereo camera synchronization",
                    status,
                    details
                )
            )

        # -----------------------------------------------------
        # CAM-FPS-001
        # -----------------------------------------------------

        if not self.fps_values:
            self.results.append(
                TestResult(
                    "CAM-FPS-001",
                    "Camera frame-rate reporting",
                    "NOT_RUN",
                    "No FPS data found."
                )
            )
        else:
            first_fps = self.fps_values[0]
            last_fps = self.fps_values[-1]

            self.results.append(
                TestResult(
                    "CAM-FPS-001",
                    "Camera frame-rate reporting",
                    "INFO",
                    f"FPS progressed from {first_fps:.2f} "
                    f"to {last_fps:.2f}. "
                    "Steady-state requirement must be defined."
                )
            )

        # -----------------------------------------------------
        # E2E-CAM-001
        # -----------------------------------------------------

        storage_ok = (
            self.raw_left
            and self.raw_right
            and self.processed_left
            and self.processed_right
        )

        if storage_ok:
            status = "PASS"
            details = (
                "Raw and processed left/right image outputs "
                "were detected in the log."
            )
        else:
            status = "FAIL"
            details = (
                f"Image storage incomplete: "
                f"raw_left={self.raw_left}, "
                f"raw_right={self.raw_right}, "
                f"processed_left={self.processed_left}, "
                f"processed_right={self.processed_right}"
            )

        self.results.append(
            TestResult(
                "E2E-CAM-001",
                "Stereo capture to image storage",
                status,
                details
            )
        )

        # -----------------------------------------------------
        # SBC-RESOURCE-001
        # -----------------------------------------------------

        if self.cpu_loads:
            max_cpu = max(self.cpu_loads)
            max_gpu = max(self.gpu_loads)
            max_memory = max(self.memory_usage)

            # CPU > 100% is not automatically a failure on
            # multicore Linux systems.
            self.results.append(
                TestResult(
                    "SBC-RESOURCE-001",
                    "SBC resource utilization",
                    "INFO",
                    f"Maximum CPU={max_cpu:.1f}%, "
                    f"GPU={max_gpu:.1f}%, "
                    f"memory={max_memory:.1f}%. "
                    "Transient CPU values above 100% are possible "
                    "on multicore systems and require correlation "
                    "with dropped frames or processing failures."
                )
            )
        else:
            self.results.append(
                TestResult(
                    "SBC-RESOURCE-001",
                    "SBC resource utilization",
                    "NOT_RUN",
                    "No resource utilization data found."
                )
            )

        # -----------------------------------------------------
        # SBC-THERMAL-001
        # -----------------------------------------------------

        thermal_fail = False
        thermal_details = []

        if self.cpu_temps:
            max_cpu_temp = max(self.cpu_temps)

            if max_cpu_temp >= CPU_CRITICAL_TEMP_C:
                thermal_fail = True

            thermal_details.append(
                f"CPU max={max_cpu_temp:.1f}C"
            )

        if self.gpu_temps:
            max_gpu_temp = max(self.gpu_temps)

            if max_gpu_temp >= GPU_CRITICAL_TEMP_C:
                thermal_fail = True

            thermal_details.append(
                f"GPU max={max_gpu_temp:.1f}C"
            )

        if thermal_details:
            status = "FAIL" if thermal_fail else "PASS"

            self.results.append(
                TestResult(
                    "SBC-THERMAL-001",
                    "SBC thermal monitoring",
                    status,
                    ", ".join(thermal_details)
                )
            )
        else:
            self.results.append(
                TestResult(
                    "SBC-THERMAL-001",
                    "SBC thermal monitoring",
                    "NOT_RUN",
                    "No thermal data found."
                )
            )

        # -----------------------------------------------------
        # SSD-THERMAL-001
        # -----------------------------------------------------

        if self.nvme_temps:
            max_nvme = max(self.nvme_temps)

            if max_nvme >= NVME_CRITICAL_TEMP_C:
                status = "FAIL"
            else:
                status = "PASS"

            self.results.append(
                TestResult(
                    "SSD-THERMAL-001",
                    "NVMe thermal status",
                    status,
                    f"Maximum NVMe temperature = "
                    f"{max_nvme:.1f}C, "
                    f"critical limit = {NVME_CRITICAL_TEMP_C:.1f}C."
                )
            )
        else:
            self.results.append(
                TestResult(
                    "SSD-THERMAL-001",
                    "NVMe thermal status",
                    "NOT_RUN",
                    "No NVMe temperature data found."
                )
            )

        # -----------------------------------------------------
        # TIME-001
        # -----------------------------------------------------

        if self.time_sync_found:
            self.results.append(
                TestResult(
                    "TIME-001",
                    "Jetson System time synchronization",
                    "PASS",
                    f"RMS clock offset = "
                    f"{self.time_sync_offset:.9f} sec."
                )
            )
        else:
            self.results.append(
                TestResult(
                    "TIME-001",
                    "Jetson System time synchronization",
                    "NOT_RUN",
                    "No time synchronization data found."
                )
            )

    # ---------------------------------------------------------
    # Reporting
    # ---------------------------------------------------------

    def overall_status(self):
        failures = [
            result for result in self.results
            if result.status == "FAIL"
        ]

        return "FAIL" if failures else "PASS"

    def print_report(self):
        print()
        print("=" * 72)
        print("EMBEDDED SYSTEM LOG ANALYSIS")
        print("=" * 72)

        for result in self.results:
            print(
                f"{result.test_id:<20} "
                f"{result.status:<10} "
                f"{result.description}"
            )

            print(f"  {result.details}")

        print("-" * 72)
        print(f"OVERALL RESULT: {self.overall_status()}")
        print("=" * 72)

    def json_report(self):
        return {
            "overall_status": self.overall_status(),
            "tests": [
                asdict(result)
                for result in self.results
            ]
        }


def main():
    parser = argparse.ArgumentParser(
        description="Analyze Voyis embedded-system logs."
    )

    parser.add_argument(
        "logfile",
        type=Path,
        help="Path to system log"
    )

    parser.add_argument(
        "--json",
        type=Path,
        help="Write JSON test result"
    )

    args = parser.parse_args()

    if not args.logfile.exists():
        print(f"ERROR: Log file not found: {args.logfile}")
        return 2

    log_text = args.logfile.read_text(
        encoding="utf-8",
        errors="replace"
    )

    analyzer = LogAnalyzer(log_text)
    analyzer.analyze()
    analyzer.print_report()

    if args.json:
        args.json.write_text(
            json.dumps(
                analyzer.json_report(),
                indent=2
            ),
            encoding="utf-8"
        )

        print(f"\nJSON report written to: {args.json}")

    # Important for CI/CD:
    # return non-zero if a test failed.
    return 1 if analyzer.overall_status() == "FAIL" else 0


if __name__ == "__main__":
    sys.exit(main())