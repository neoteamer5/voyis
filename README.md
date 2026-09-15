# Embedded System Log Analysis

This project provides Python tools for analyzing embedded-system logs and generating automated QA test results.

## Project Structure

```text
.
├── CaptureAnalysis.py
├── SystemHealth.py
├── application_runtime.log
├── system_status.log
└── README.md
```

## Requirements

* Python 3.9 or newer
* No third-party Python packages are required

Check the Python version:

```bash
python3 --version
```

---

# Log Files

The analysis uses two different log files because they contain different types of information.

| Log File                  | Purpose                                                             | Analysis Script      |
| ------------------------- | ------------------------------------------------------------------- | -------------------- |
| `application_runtime.log` | Camera capture sessions, capture timing, API errors, LED errors     | `CaptureAnalysis.py` |
| `system_status.log`       | SBC resource usage, temperatures, NVMe status, time synchronization | `SystemHealth.py`    |

The logs are analyzed independently.

---

# 1. Camera Capture Analysis

## Script

```text
CaptureAnalysis.py
```

## Input

```text
application_runtime.log
```

This log contains application-level camera events such as:

```text
Capturing 10 images at 1 Hz save rate (deadline: 15 s)
```

and:

```text
Capture Session: 10 images in 10.38 s
```

The script analyzes:

* Number of capture sessions
* Expected image count
* Actual image count
* Capture duration
* Capture deadline
* LED failures
* API request timeouts
* Incomplete capture sessions

## Run

```bash
python3 CaptureAnalysis.py application_runtime.log
```

For example, if the supplied log is named `discovery_headless.log`:

```bash
python3 CaptureAnalysis.py discovery_headless.log
```

## Verdict

A capture is reported as **PASS** when:

1. The expected number of images is captured.
2. The capture finishes within the specified deadline.
3. No API timeout is reported.
4. No LED control failure is reported.

A capture is reported as **FAIL** when one or more requirements are violated.

A capture is reported as **INCOMPLETE** when the capture starts but no corresponding completion event is found.

---

# 2. System Health Analysis

## Script

```text
SystemHealth.py
```

## Input

```text
system_status.log
```

This log contains system-level health information from the Jetson, including:

* CPU utilization
* GPU utilization
* Memory utilization
* Disk utilization
* Network utilization
* CPU temperature
* GPU temperature
* PMIC temperature
* NVMe temperature
* System time synchronization

## Run

```bash
python3 SystemHealth.py system_status.log
```

## Example Output

```text
SBC-RESOURCE-001    INFO
  CPU max: 208%
  GPU max: 47%
  Memory usage max: 32%
  Disk usage max: 1%
  Network usage max: 0 Mbps

SBC-THERMAL-001    PASS
  CPU max: 31.5 C
  GPU max: 30.0 C
  PMIC max: 50.0 C

SSD-THERMAL-001    PASS
  NVMe temperature max: 26.0 C
  Warning limit: 52.0 C
  Critical limit: 54.0 C

TIME-001            PASS
  RMS offset: 0 seconds
  Reference ID: 7F7F0101
  Stratum: 10
  Frequency: 9.849 ppm slow
```

---

# 3. Running the Complete Analysis

Run the two analyses separately.

### Step 1 — Analyze camera captures

```bash
python3 CaptureAnalysis.py application_runtime.log
```

### Step 2 — Analyze system health

```bash
python3 SystemHealth.py system_status.log
```

The two scripts have independent `main()` functions and can therefore be executed independently.

---

# 4. Analysis Flow

```text
                 Embedded System
                       |
              +--------+--------+
              |                 |
              v                 v
    application_runtime.log   system_status.log
              |                 |
              v                 v
    CaptureAnalysis.py       SystemHealth.py
              |                 |
              v                 v
       Capture Results       System Health
       PASS/FAIL             PASS/INFO
              |                 |
              +--------+--------+
                       |
                       v
                  QA Report
```

---

# 5. PASS / FAIL / INCOMPLETE / INFO

| Result       | Meaning                                                                         |
| ------------ | ------------------------------------------------------------------------------- |
| `PASS`       | Available log evidence satisfies the defined test criteria.                     |
| `FAIL`       | Log evidence shows that a defined test criterion was violated.                  |
| `INCOMPLETE` | The test started but there is insufficient evidence that it completed normally. |
| `INFO`       | Data was successfully extracted, but no pass/fail requirement was defined.      |

---

# 6. Log-Based Test Automation

The scripts use the application logs as **test oracles**.

For example:

```text
Capturing 10 images at 1 Hz save rate (deadline: 15 s)
```

defines the expected behavior.

The corresponding result:

```text
Capture Session: 10 images in 10.38 s
```

provides the observed behavior.

The Python test automation compares the expected and observed values and generates the test verdict.

This approach allows the test to be repeated consistently without requiring manual inspection of the complete log.

---

# 7. Important Testing Limitations

Log analysis can verify software-observable behavior, but it cannot prove every physical hardware requirement.

Examples:

* GPIO electrical timing may require an oscilloscope or logic analyzer.
* Camera optical quality may require image-quality analysis or manual inspection.
* Physical camera synchronization may require external timing instrumentation.
* Hardware failures that produce no observable log information cannot be conclusively diagnosed from logs alone.

For these cases, the test should explicitly identify the additional equipment or observability required.

---

# 8. Assumptions

The analysis assumes:

* The log format remains consistent with the supplied test logs.
* Camera capture events are recorded in `application_runtime.log`.
* System health information is recorded in `system_status.log`.
* Capture deadlines and expected image counts reported in the log represent the intended test configuration.
* Product-specific limits should ultimately come from formal requirements rather than being permanently hard-coded in the test scripts.

---

# 9. Recommended Execution

From the project directory:

```bash
python3 CaptureAnalysis.py application_runtime.log
python3 SystemHealth.py system_status.log
```

For the supplied Voyis capture log, if it is named `discovery_headless.log`:

```bash
python3 CaptureAnalysis.py discovery_headless.log
```

The resulting reports provide separate evidence for:

1. **Camera/application behavior**
2. **SBC/system health**

These results can then be incorporated into the overall system validation report.
