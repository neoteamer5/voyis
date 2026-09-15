## Log Analysis

### Capture Analysis

Analyze the application runtime log:

```bash
python3 CaptureAnalysis.py application_runtime.log
```

This prints the capture summary to the console and generates:

```text
capture_analysis.md
```

To specify a custom Markdown report filename:

```bash
python3 CaptureAnalysis.py application_runtime.log voyis_capture_report.md
```

### System Health Analysis

Run the system health analyzer:

```bash
python3 SystemHealth.py system_status.log
```

### Example

```bash
python3 CaptureAnalysis.py application_runtime.log
python3 SystemHealth.py system_status.log
```
