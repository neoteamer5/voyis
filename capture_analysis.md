# Capture Analysis Report

**Input log:** `application_runtime.log`

**Overall result:** **FAIL**

## Requirements

- Expected stereo pairs: **10**
- Maximum power-on to completion time: **60 s**
- Application capture deadline is evaluated separately from the 60-second system requirement.
- `Device detected` is used as the observable power-on reference because an explicit electrical power-on timestamp is not present in the application log.

## Summary

| Capture | Result | Images | Duration | Power-on → Completion |
|---:|---|---:|---:|---:|
| 1 | INCOMPLETE | N/A | N/A | N/A |
| 2 | INCOMPLETE | N/A | N/A | N/A |
| 3 | FAIL | 10/10 | 9.88s | 13.99s |
| 4 | FAIL | 10/10 | 9.69s | 13.49s |
| 5 | FAIL | 10/10 | 10.18s | 13.63s |
| 6 | FAIL | 10/10 | 10.09s | 14.28s |
| 7 | FAIL | 10/10 | 10.08s | 14.04s |
| 8 | FAIL | 10/10 | 10.18s | 14.18s |
| 9 | FAIL | 10/10 | 9.88s | 13.36s |
| 10 | FAIL | 10/10 | 9.98s | 13.85s |
| 11 | FAIL | 10/10 | 10.38s | 13.79s |
| 12 | FAIL | 10/10 | 9.66s | 13.97s |
| 13 | FAIL | 10/10 | 9.98s | 14.28s |
| 14 | FAIL | 10/10 | 10.08s | 13.55s |
| 15 | FAIL | 10/10 | 9.38s | 13.13s |
| 16 | FAIL | 10/10 | 10.18s | 13.55s |
| 17 | FAIL | 10/10 | 9.99s | 13.64s |
| 18 | FAIL | 10/10 | 9.19s | 12.61s |
| 19 | FAIL | 10/10 | 9.88s | 13.26s |
| 20 | FAIL | 10/10 | 10.38s | 14.60s |
| 21 | INCOMPLETE | N/A | N/A | N/A |
| 22 | FAIL | 22/10 | 21.61s | 25.02s |
| 23 | FAIL | 10/10 | 9.78s | 13.64s |
| 24 | FAIL | 10/10 | 9.98s | 14.15s |
| 25 | FAIL | 10/10 | 9.58s | 13.61s |
| 26 | FAIL | 10/10 | 9.68s | 13.23s |
| 27 | FAIL | 10/10 | 9.98s | 13.45s |
| 28 | FAIL | 10/10 | 10.08s | 13.43s |
| 29 | FAIL | 10/10 | 9.87s | 13.69s |
| 30 | FAIL | 10/10 | 10.08s | 13.45s |
| 31 | FAIL | 10/10 | 9.29s | 13.48s |
| 32 | FAIL | 3/10 | 17.06s | 20.96s |
| 33 | FAIL | 10/10 | 9.58s | 13.27s |
| 34 | FAIL | 10/10 | 9.39s | 12.81s |
| 35 | FAIL | 10/10 | 9.88s | 13.47s |
| 36 | FAIL | 10/10 | 9.88s | 13.37s |
| 37 | FAIL | 10/10 | 9.88s | 13.95s |
| 38 | FAIL | 10/10 | 9.49s | 13.21s |
| 39 | FAIL | 10/10 | 9.98s | 14.17s |
| 40 | FAIL | 10/10 | 10.18s | 13.68s |
| 41 | FAIL | 10/10 | 10.08s | 13.72s |
| 42 | FAIL | 10/10 | 9.98s | 13.46s |
| 43 | FAIL | 10/10 | 9.98s | 13.66s |
| 44 | FAIL | 10/10 | 9.78s | 13.40s |
| 45 | FAIL | 10/10 | 10.18s | 13.54s |
| 46 | FAIL | 10/10 | 10.18s | 14.49s |
| 47 | FAIL | 10/10 | 9.28s | 12.67s |
| 48 | FAIL | 10/10 | 9.77s | 13.35s |
| 49 | FAIL | 10/10 | 10.09s | 13.45s |
| 50 | FAIL | 10/10 | 9.48s | 13.72s |
| 51 | FAIL | 10/10 | 9.28s | 12.97s |

## Capture #1

**Start time:** `2026-05-27 16:06:03.017`

### Application-Level Validation

- Image count: **INCOMPLETE**
- Application deadline (0s): **NOT VERIFIED**

### System-Level Validation

- 60-second requirement: **NOT VERIFIED**

> Note: the log does not contain an explicit electrical power-on timestamp. Device detection is therefore used as an observable proxy.

### Raw Image Validation

- Raw saving enabled: **FAIL**
- Raw Left files observed: 0
- Raw Right files observed: 0
- Raw stereo-pair evidence: **NOT VERIFIED**

### Processed Image Validation

- Processed saving enabled: **FAIL**
- Processed Left files observed: 0
- Processed Right files observed: 0
- Processed stereo-pair evidence: **NOT VERIFIED**

### Error Checks

- LED failure: **PASS**
- API timeout: **PASS**

### Capture Verdict

**Result:** **INCOMPLETE**

**Reason:** No capture completion record.

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #2

**Start time:** `2026-05-27 16:07:10.102`

**Device detected:** `2026-05-27 16:07:26.665`

### Application-Level Validation

- Image count: **INCOMPLETE**
- Application deadline (0s): **NOT VERIFIED**

### System-Level Validation

- 60-second requirement: **NOT VERIFIED**

> Note: the log does not contain an explicit electrical power-on timestamp. Device detection is therefore used as an observable proxy.

### Raw Image Validation

- Raw saving enabled: **PASS**
- Raw Left files observed: 0
- Raw Right files observed: 0
- Raw stereo-pair evidence: **NOT VERIFIED**

### Processed Image Validation

- Processed saving enabled: **PASS**
- Processed Left files observed: 0
- Processed Right files observed: 0
- Processed stereo-pair evidence: **NOT VERIFIED**

### Error Checks

- LED failure: **PASS**
- API timeout: **PASS**

### Capture Verdict

**Result:** **INCOMPLETE**

**Reason:** No capture completion record.

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #3

**Start time:** `2026-05-27 16:11:10.390`

**Device detected:** `2026-05-27 16:11:27.396`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (0s): **FAIL**
  - Observed duration: 9.88s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.99s

> Note: the log does not contain an explicit electrical power-on timestamp. Device detection is therefore used as an observable proxy.

### Raw Image Validation

- Raw saving enabled: **PASS**
- Raw Left files observed: 0
- Raw Right files observed: 0
- Raw stereo-pair evidence: **NOT VERIFIED**

### Processed Image Validation

- Processed saving enabled: **PASS**
- Processed Left files observed: 0
- Processed Right files observed: 0
- Processed stereo-pair evidence: **NOT VERIFIED**

### Error Checks

- LED failure: **PASS**
- API timeout: **PASS**

### Capture Verdict

**Result:** **FAIL**

**Reason:** capture duration 9.88s exceeded application deadline 0.00s

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #4

**Start time:** `2026-05-27 16:15:08.933`

**Device detected:** `2026-05-27 16:15:25.824`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (0s): **FAIL**
  - Observed duration: 9.69s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.49s

> Note: the log does not contain an explicit electrical power-on timestamp. Device detection is therefore used as an observable proxy.

### Raw Image Validation

- Raw saving enabled: **PASS**
- Raw Left files observed: 0
- Raw Right files observed: 0
- Raw stereo-pair evidence: **NOT VERIFIED**

### Processed Image Validation

- Processed saving enabled: **PASS**
- Processed Left files observed: 0
- Processed Right files observed: 0
- Processed stereo-pair evidence: **NOT VERIFIED**

### Error Checks

- LED failure: **PASS**
- API timeout: **PASS**

### Capture Verdict

**Result:** **FAIL**

**Reason:** capture duration 9.69s exceeded application deadline 0.00s

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #5

**Start time:** `2026-05-27 16:19:10.290`

**Device detected:** `2026-05-27 16:19:26.786`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (0s): **FAIL**
  - Observed duration: 10.18s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.63s

> Note: the log does not contain an explicit electrical power-on timestamp. Device detection is therefore used as an observable proxy.

### Raw Image Validation

- Raw saving enabled: **PASS**
- Raw Left files observed: 0
- Raw Right files observed: 0
- Raw stereo-pair evidence: **NOT VERIFIED**

### Processed Image Validation

- Processed saving enabled: **PASS**
- Processed Left files observed: 0
- Processed Right files observed: 0
- Processed stereo-pair evidence: **NOT VERIFIED**

### Error Checks

- LED failure: **PASS**
- API timeout: **PASS**

### Capture Verdict

**Result:** **FAIL**

**Reason:** capture duration 10.18s exceeded application deadline 0.00s

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #6

**Start time:** `2026-05-27 16:23:09.367`

**Device detected:** `2026-05-27 16:23:26.023`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (0s): **FAIL**
  - Observed duration: 10.09s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 14.28s

> Note: the log does not contain an explicit electrical power-on timestamp. Device detection is therefore used as an observable proxy.

### Raw Image Validation

- Raw saving enabled: **PASS**
- Raw Left files observed: 0
- Raw Right files observed: 0
- Raw stereo-pair evidence: **NOT VERIFIED**

### Processed Image Validation

- Processed saving enabled: **PASS**
- Processed Left files observed: 0
- Processed Right files observed: 0
- Processed stereo-pair evidence: **NOT VERIFIED**

### Error Checks

- LED failure: **PASS**
- API timeout: **PASS**

### Capture Verdict

**Result:** **FAIL**

**Reason:** capture duration 10.09s exceeded application deadline 0.00s

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #7

**Start time:** `2026-05-27 16:27:11.133`

**Device detected:** `2026-05-27 16:27:28.228`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (0s): **FAIL**
  - Observed duration: 10.08s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 14.04s

> Note: the log does not contain an explicit electrical power-on timestamp. Device detection is therefore used as an observable proxy.

### Raw Image Validation

- Raw saving enabled: **PASS**
- Raw Left files observed: 0
- Raw Right files observed: 0
- Raw stereo-pair evidence: **NOT VERIFIED**

### Processed Image Validation

- Processed saving enabled: **PASS**
- Processed Left files observed: 0
- Processed Right files observed: 0
- Processed stereo-pair evidence: **NOT VERIFIED**

### Error Checks

- LED failure: **PASS**
- API timeout: **PASS**

### Capture Verdict

**Result:** **FAIL**

**Reason:** capture duration 10.08s exceeded application deadline 0.00s

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #8

**Start time:** `2026-05-27 16:31:11.581`

**Device detected:** `2026-05-27 16:31:28.144`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (0s): **FAIL**
  - Observed duration: 10.18s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 14.18s

> Note: the log does not contain an explicit electrical power-on timestamp. Device detection is therefore used as an observable proxy.

### Raw Image Validation

- Raw saving enabled: **PASS**
- Raw Left files observed: 0
- Raw Right files observed: 0
- Raw stereo-pair evidence: **NOT VERIFIED**

### Processed Image Validation

- Processed saving enabled: **PASS**
- Processed Left files observed: 0
- Processed Right files observed: 0
- Processed stereo-pair evidence: **NOT VERIFIED**

### Error Checks

- LED failure: **PASS**
- API timeout: **PASS**

### Capture Verdict

**Result:** **FAIL**

**Reason:** capture duration 10.18s exceeded application deadline 0.00s

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #9

**Start time:** `2026-05-27 16:35:11.321`

**Device detected:** `2026-05-27 16:35:27.938`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (0s): **FAIL**
  - Observed duration: 9.88s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.36s

> Note: the log does not contain an explicit electrical power-on timestamp. Device detection is therefore used as an observable proxy.

### Raw Image Validation

- Raw saving enabled: **PASS**
- Raw Left files observed: 0
- Raw Right files observed: 0
- Raw stereo-pair evidence: **NOT VERIFIED**

### Processed Image Validation

- Processed saving enabled: **PASS**
- Processed Left files observed: 0
- Processed Right files observed: 0
- Processed stereo-pair evidence: **NOT VERIFIED**

### Error Checks

- LED failure: **PASS**
- API timeout: **PASS**

### Capture Verdict

**Result:** **FAIL**

**Reason:** capture duration 9.88s exceeded application deadline 0.00s

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #10

**Start time:** `2026-05-27 16:39:10.360`

**Device detected:** `2026-05-27 16:39:26.478`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (0s): **FAIL**
  - Observed duration: 9.98s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.85s

> Note: the log does not contain an explicit electrical power-on timestamp. Device detection is therefore used as an observable proxy.

### Raw Image Validation

- Raw saving enabled: **PASS**
- Raw Left files observed: 0
- Raw Right files observed: 0
- Raw stereo-pair evidence: **NOT VERIFIED**

### Processed Image Validation

- Processed saving enabled: **PASS**
- Processed Left files observed: 0
- Processed Right files observed: 0
- Processed stereo-pair evidence: **NOT VERIFIED**

### Error Checks

- LED failure: **PASS**
- API timeout: **PASS**

### Capture Verdict

**Result:** **FAIL**

**Reason:** capture duration 9.98s exceeded application deadline 0.00s

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #11

**Start time:** `2026-05-27 16:43:09.530`

**Device detected:** `2026-05-27 16:43:25.819`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (0s): **FAIL**
  - Observed duration: 10.38s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.79s

> Note: the log does not contain an explicit electrical power-on timestamp. Device detection is therefore used as an observable proxy.

### Raw Image Validation

- Raw saving enabled: **PASS**
- Raw Left files observed: 0
- Raw Right files observed: 0
- Raw stereo-pair evidence: **NOT VERIFIED**

### Processed Image Validation

- Processed saving enabled: **PASS**
- Processed Left files observed: 0
- Processed Right files observed: 0
- Processed stereo-pair evidence: **NOT VERIFIED**

### Error Checks

- LED failure: **PASS**
- API timeout: **PASS**

### Capture Verdict

**Result:** **FAIL**

**Reason:** capture duration 10.38s exceeded application deadline 0.00s

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #12

**Start time:** `2026-05-27 16:47:10.537`

**Device detected:** `2026-05-27 16:47:27.432`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (0s): **FAIL**
  - Observed duration: 9.66s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.97s

> Note: the log does not contain an explicit electrical power-on timestamp. Device detection is therefore used as an observable proxy.

### Raw Image Validation

- Raw saving enabled: **PASS**
- Raw Left files observed: 0
- Raw Right files observed: 0
- Raw stereo-pair evidence: **NOT VERIFIED**

### Processed Image Validation

- Processed saving enabled: **PASS**
- Processed Left files observed: 0
- Processed Right files observed: 0
- Processed stereo-pair evidence: **NOT VERIFIED**

### Error Checks

- LED failure: **PASS**
- API timeout: **PASS**

### Capture Verdict

**Result:** **FAIL**

**Reason:** capture duration 9.66s exceeded application deadline 0.00s

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #13

**Start time:** `2026-05-27 16:51:09.468`

**Device detected:** `2026-05-27 16:51:26.191`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (0s): **FAIL**
  - Observed duration: 9.98s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 14.28s

> Note: the log does not contain an explicit electrical power-on timestamp. Device detection is therefore used as an observable proxy.

### Raw Image Validation

- Raw saving enabled: **PASS**
- Raw Left files observed: 0
- Raw Right files observed: 0
- Raw stereo-pair evidence: **NOT VERIFIED**

### Processed Image Validation

- Processed saving enabled: **PASS**
- Processed Left files observed: 0
- Processed Right files observed: 0
- Processed stereo-pair evidence: **NOT VERIFIED**

### Error Checks

- LED failure: **PASS**
- API timeout: **PASS**

### Capture Verdict

**Result:** **FAIL**

**Reason:** capture duration 9.98s exceeded application deadline 0.00s

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #14

**Start time:** `2026-05-27 16:55:10.104`

**Device detected:** `2026-05-27 16:55:26.836`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (0s): **FAIL**
  - Observed duration: 10.08s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.55s

> Note: the log does not contain an explicit electrical power-on timestamp. Device detection is therefore used as an observable proxy.

### Raw Image Validation

- Raw saving enabled: **PASS**
- Raw Left files observed: 0
- Raw Right files observed: 0
- Raw stereo-pair evidence: **NOT VERIFIED**

### Processed Image Validation

- Processed saving enabled: **PASS**
- Processed Left files observed: 0
- Processed Right files observed: 0
- Processed stereo-pair evidence: **NOT VERIFIED**

### Error Checks

- LED failure: **PASS**
- API timeout: **PASS**

### Capture Verdict

**Result:** **FAIL**

**Reason:** capture duration 10.08s exceeded application deadline 0.00s

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #15

**Start time:** `2026-05-27 16:59:09.946`

**Device detected:** `2026-05-27 16:59:27.232`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (0s): **FAIL**
  - Observed duration: 9.38s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.13s

> Note: the log does not contain an explicit electrical power-on timestamp. Device detection is therefore used as an observable proxy.

### Raw Image Validation

- Raw saving enabled: **PASS**
- Raw Left files observed: 0
- Raw Right files observed: 0
- Raw stereo-pair evidence: **NOT VERIFIED**

### Processed Image Validation

- Processed saving enabled: **PASS**
- Processed Left files observed: 0
- Processed Right files observed: 0
- Processed stereo-pair evidence: **NOT VERIFIED**

### Error Checks

- LED failure: **PASS**
- API timeout: **PASS**

### Capture Verdict

**Result:** **FAIL**

**Reason:** capture duration 9.38s exceeded application deadline 0.00s

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #16

**Start time:** `2026-05-27 17:03:09.480`

**Device detected:** `2026-05-27 17:03:25.953`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (0s): **FAIL**
  - Observed duration: 10.18s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.55s

> Note: the log does not contain an explicit electrical power-on timestamp. Device detection is therefore used as an observable proxy.

### Raw Image Validation

- Raw saving enabled: **PASS**
- Raw Left files observed: 0
- Raw Right files observed: 0
- Raw stereo-pair evidence: **NOT VERIFIED**

### Processed Image Validation

- Processed saving enabled: **PASS**
- Processed Left files observed: 0
- Processed Right files observed: 0
- Processed stereo-pair evidence: **NOT VERIFIED**

### Error Checks

- LED failure: **PASS**
- API timeout: **PASS**

### Capture Verdict

**Result:** **FAIL**

**Reason:** capture duration 10.18s exceeded application deadline 0.00s

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #17

**Start time:** `2026-05-27 17:07:09.065`

**Device detected:** `2026-05-27 17:07:25.845`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (0s): **FAIL**
  - Observed duration: 9.99s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.64s

> Note: the log does not contain an explicit electrical power-on timestamp. Device detection is therefore used as an observable proxy.

### Raw Image Validation

- Raw saving enabled: **PASS**
- Raw Left files observed: 0
- Raw Right files observed: 0
- Raw stereo-pair evidence: **NOT VERIFIED**

### Processed Image Validation

- Processed saving enabled: **PASS**
- Processed Left files observed: 0
- Processed Right files observed: 0
- Processed stereo-pair evidence: **NOT VERIFIED**

### Error Checks

- LED failure: **PASS**
- API timeout: **PASS**

### Capture Verdict

**Result:** **FAIL**

**Reason:** capture duration 9.99s exceeded application deadline 0.00s

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #18

**Start time:** `2026-05-27 17:11:08.367`

**Device detected:** `2026-05-27 17:11:25.692`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (0s): **FAIL**
  - Observed duration: 9.19s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 12.61s

> Note: the log does not contain an explicit electrical power-on timestamp. Device detection is therefore used as an observable proxy.

### Raw Image Validation

- Raw saving enabled: **PASS**
- Raw Left files observed: 0
- Raw Right files observed: 0
- Raw stereo-pair evidence: **NOT VERIFIED**

### Processed Image Validation

- Processed saving enabled: **PASS**
- Processed Left files observed: 0
- Processed Right files observed: 0
- Processed stereo-pair evidence: **NOT VERIFIED**

### Error Checks

- LED failure: **PASS**
- API timeout: **PASS**

### Capture Verdict

**Result:** **FAIL**

**Reason:** capture duration 9.19s exceeded application deadline 0.00s

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #19

**Start time:** `2026-05-27 17:15:09.249`

**Device detected:** `2026-05-27 17:15:26.013`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (0s): **FAIL**
  - Observed duration: 9.88s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.26s

> Note: the log does not contain an explicit electrical power-on timestamp. Device detection is therefore used as an observable proxy.

### Raw Image Validation

- Raw saving enabled: **PASS**
- Raw Left files observed: 0
- Raw Right files observed: 0
- Raw stereo-pair evidence: **NOT VERIFIED**

### Processed Image Validation

- Processed saving enabled: **PASS**
- Processed Left files observed: 0
- Processed Right files observed: 0
- Processed stereo-pair evidence: **NOT VERIFIED**

### Error Checks

- LED failure: **PASS**
- API timeout: **PASS**

### Capture Verdict

**Result:** **FAIL**

**Reason:** capture duration 9.88s exceeded application deadline 0.00s

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #20

**Start time:** `2026-05-27 17:19:08.108`

**Device detected:** `2026-05-27 17:19:24.949`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (0s): **FAIL**
  - Observed duration: 10.38s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 14.60s

> Note: the log does not contain an explicit electrical power-on timestamp. Device detection is therefore used as an observable proxy.

### Raw Image Validation

- Raw saving enabled: **PASS**
- Raw Left files observed: 0
- Raw Right files observed: 0
- Raw stereo-pair evidence: **NOT VERIFIED**

### Processed Image Validation

- Processed saving enabled: **PASS**
- Processed Left files observed: 0
- Processed Right files observed: 0
- Processed stereo-pair evidence: **NOT VERIFIED**

### Error Checks

- LED failure: **PASS**
- API timeout: **PASS**

### Capture Verdict

**Result:** **FAIL**

**Reason:** capture duration 10.38s exceeded application deadline 0.00s

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #21

**Start time:** `2026-05-27 17:23:08.464`

**Device detected:** `2026-05-27 17:23:25.349`

### Application-Level Validation

- Image count: **INCOMPLETE**
- Application deadline (0s): **NOT VERIFIED**

### System-Level Validation

- 60-second requirement: **NOT VERIFIED**

> Note: the log does not contain an explicit electrical power-on timestamp. Device detection is therefore used as an observable proxy.

### Raw Image Validation

- Raw saving enabled: **PASS**
- Raw Left files observed: 0
- Raw Right files observed: 0
- Raw stereo-pair evidence: **NOT VERIFIED**

### Processed Image Validation

- Processed saving enabled: **PASS**
- Processed Left files observed: 0
- Processed Right files observed: 0
- Processed stereo-pair evidence: **NOT VERIFIED**

### Error Checks

- LED failure: **PASS**
- API timeout: **PASS**

### Capture Verdict

**Result:** **INCOMPLETE**

**Reason:** No capture completion record.

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #22

**Start time:** `2026-05-27 17:31:08.968`

**Device detected:** `2026-05-27 17:31:25.741`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 22
- Application deadline (0s): **FAIL**
  - Observed duration: 21.61s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 25.02s

> Note: the log does not contain an explicit electrical power-on timestamp. Device detection is therefore used as an observable proxy.

### Raw Image Validation

- Raw saving enabled: **PASS**
- Raw Left files observed: 0
- Raw Right files observed: 0
- Raw stereo-pair evidence: **NOT VERIFIED**

### Processed Image Validation

- Processed saving enabled: **PASS**
- Processed Left files observed: 0
- Processed Right files observed: 0
- Processed stereo-pair evidence: **NOT VERIFIED**

### Error Checks

- LED failure: **FAIL**
- API timeout: **FAIL**

### Capture Verdict

**Result:** **FAIL**

**Reason:** expected 10 images, observed 22; capture duration 21.61s exceeded application deadline 0.00s; LED disable failure detected; API timeout detected

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #23

**Start time:** `2026-05-27 17:35:08.100`

**Device detected:** `2026-05-27 17:35:24.618`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (0s): **FAIL**
  - Observed duration: 9.78s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.64s

> Note: the log does not contain an explicit electrical power-on timestamp. Device detection is therefore used as an observable proxy.

### Raw Image Validation

- Raw saving enabled: **PASS**
- Raw Left files observed: 0
- Raw Right files observed: 0
- Raw stereo-pair evidence: **NOT VERIFIED**

### Processed Image Validation

- Processed saving enabled: **PASS**
- Processed Left files observed: 0
- Processed Right files observed: 0
- Processed stereo-pair evidence: **NOT VERIFIED**

### Error Checks

- LED failure: **PASS**
- API timeout: **PASS**

### Capture Verdict

**Result:** **FAIL**

**Reason:** capture duration 9.78s exceeded application deadline 0.00s

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #24

**Start time:** `2026-05-27 17:39:08.212`

**Device detected:** `2026-05-27 17:39:25.130`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (0s): **FAIL**
  - Observed duration: 9.98s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 14.15s

> Note: the log does not contain an explicit electrical power-on timestamp. Device detection is therefore used as an observable proxy.

### Raw Image Validation

- Raw saving enabled: **PASS**
- Raw Left files observed: 0
- Raw Right files observed: 0
- Raw stereo-pair evidence: **NOT VERIFIED**

### Processed Image Validation

- Processed saving enabled: **PASS**
- Processed Left files observed: 0
- Processed Right files observed: 0
- Processed stereo-pair evidence: **NOT VERIFIED**

### Error Checks

- LED failure: **PASS**
- API timeout: **PASS**

### Capture Verdict

**Result:** **FAIL**

**Reason:** capture duration 9.98s exceeded application deadline 0.00s

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #25

**Start time:** `2026-05-27 17:43:08.298`

**Device detected:** `2026-05-27 17:43:24.759`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (0s): **FAIL**
  - Observed duration: 9.58s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.61s

> Note: the log does not contain an explicit electrical power-on timestamp. Device detection is therefore used as an observable proxy.

### Raw Image Validation

- Raw saving enabled: **PASS**
- Raw Left files observed: 0
- Raw Right files observed: 0
- Raw stereo-pair evidence: **NOT VERIFIED**

### Processed Image Validation

- Processed saving enabled: **PASS**
- Processed Left files observed: 0
- Processed Right files observed: 0
- Processed stereo-pair evidence: **NOT VERIFIED**

### Error Checks

- LED failure: **PASS**
- API timeout: **PASS**

### Capture Verdict

**Result:** **FAIL**

**Reason:** capture duration 9.58s exceeded application deadline 0.00s

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #26

**Start time:** `2026-05-27 17:47:09.687`

**Device detected:** `2026-05-27 17:47:26.300`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (0s): **FAIL**
  - Observed duration: 9.68s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.23s

> Note: the log does not contain an explicit electrical power-on timestamp. Device detection is therefore used as an observable proxy.

### Raw Image Validation

- Raw saving enabled: **PASS**
- Raw Left files observed: 0
- Raw Right files observed: 0
- Raw stereo-pair evidence: **NOT VERIFIED**

### Processed Image Validation

- Processed saving enabled: **PASS**
- Processed Left files observed: 0
- Processed Right files observed: 0
- Processed stereo-pair evidence: **NOT VERIFIED**

### Error Checks

- LED failure: **PASS**
- API timeout: **PASS**

### Capture Verdict

**Result:** **FAIL**

**Reason:** capture duration 9.68s exceeded application deadline 0.00s

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #27

**Start time:** `2026-05-27 17:51:09.386`

**Device detected:** `2026-05-27 17:51:25.929`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (0s): **FAIL**
  - Observed duration: 9.98s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.45s

> Note: the log does not contain an explicit electrical power-on timestamp. Device detection is therefore used as an observable proxy.

### Raw Image Validation

- Raw saving enabled: **PASS**
- Raw Left files observed: 0
- Raw Right files observed: 0
- Raw stereo-pair evidence: **NOT VERIFIED**

### Processed Image Validation

- Processed saving enabled: **PASS**
- Processed Left files observed: 0
- Processed Right files observed: 0
- Processed stereo-pair evidence: **NOT VERIFIED**

### Error Checks

- LED failure: **PASS**
- API timeout: **PASS**

### Capture Verdict

**Result:** **FAIL**

**Reason:** capture duration 9.98s exceeded application deadline 0.00s

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #28

**Start time:** `2026-05-27 17:55:10.275`

**Device detected:** `2026-05-27 17:55:26.943`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (0s): **FAIL**
  - Observed duration: 10.08s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.43s

> Note: the log does not contain an explicit electrical power-on timestamp. Device detection is therefore used as an observable proxy.

### Raw Image Validation

- Raw saving enabled: **PASS**
- Raw Left files observed: 0
- Raw Right files observed: 0
- Raw stereo-pair evidence: **NOT VERIFIED**

### Processed Image Validation

- Processed saving enabled: **PASS**
- Processed Left files observed: 0
- Processed Right files observed: 0
- Processed stereo-pair evidence: **NOT VERIFIED**

### Error Checks

- LED failure: **PASS**
- API timeout: **PASS**

### Capture Verdict

**Result:** **FAIL**

**Reason:** capture duration 10.08s exceeded application deadline 0.00s

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #29

**Start time:** `2026-05-27 17:59:10.257`

**Device detected:** `2026-05-27 17:59:26.786`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (0s): **FAIL**
  - Observed duration: 9.87s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.69s

> Note: the log does not contain an explicit electrical power-on timestamp. Device detection is therefore used as an observable proxy.

### Raw Image Validation

- Raw saving enabled: **PASS**
- Raw Left files observed: 0
- Raw Right files observed: 0
- Raw stereo-pair evidence: **NOT VERIFIED**

### Processed Image Validation

- Processed saving enabled: **PASS**
- Processed Left files observed: 0
- Processed Right files observed: 0
- Processed stereo-pair evidence: **NOT VERIFIED**

### Error Checks

- LED failure: **PASS**
- API timeout: **PASS**

### Capture Verdict

**Result:** **FAIL**

**Reason:** capture duration 9.87s exceeded application deadline 0.00s

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #30

**Start time:** `2026-05-27 18:03:09.263`

**Device detected:** `2026-05-27 18:03:26.059`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (0s): **FAIL**
  - Observed duration: 10.08s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.45s

> Note: the log does not contain an explicit electrical power-on timestamp. Device detection is therefore used as an observable proxy.

### Raw Image Validation

- Raw saving enabled: **PASS**
- Raw Left files observed: 0
- Raw Right files observed: 0
- Raw stereo-pair evidence: **NOT VERIFIED**

### Processed Image Validation

- Processed saving enabled: **PASS**
- Processed Left files observed: 0
- Processed Right files observed: 0
- Processed stereo-pair evidence: **NOT VERIFIED**

### Error Checks

- LED failure: **PASS**
- API timeout: **PASS**

### Capture Verdict

**Result:** **FAIL**

**Reason:** capture duration 10.08s exceeded application deadline 0.00s

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #31

**Start time:** `2026-05-27 18:07:10.127`

**Device detected:** `2026-05-27 18:07:26.909`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (0s): **FAIL**
  - Observed duration: 9.29s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.48s

> Note: the log does not contain an explicit electrical power-on timestamp. Device detection is therefore used as an observable proxy.

### Raw Image Validation

- Raw saving enabled: **PASS**
- Raw Left files observed: 0
- Raw Right files observed: 0
- Raw stereo-pair evidence: **NOT VERIFIED**

### Processed Image Validation

- Processed saving enabled: **PASS**
- Processed Left files observed: 0
- Processed Right files observed: 0
- Processed stereo-pair evidence: **NOT VERIFIED**

### Error Checks

- LED failure: **PASS**
- API timeout: **PASS**

### Capture Verdict

**Result:** **FAIL**

**Reason:** capture duration 9.29s exceeded application deadline 0.00s

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #32

**Start time:** `2026-05-27 18:11:10.246`

**Device detected:** `2026-05-27 18:11:27.444`

### Application-Level Validation

- Image count: **FAIL**
  - Expected: 10
  - Observed: 3
- Application deadline (0s): **FAIL**
  - Observed duration: 17.06s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 20.96s

> Note: the log does not contain an explicit electrical power-on timestamp. Device detection is therefore used as an observable proxy.

### Raw Image Validation

- Raw saving enabled: **PASS**
- Raw Left files observed: 0
- Raw Right files observed: 0
- Raw stereo-pair evidence: **NOT VERIFIED**

### Processed Image Validation

- Processed saving enabled: **PASS**
- Processed Left files observed: 0
- Processed Right files observed: 0
- Processed stereo-pair evidence: **NOT VERIFIED**

### Error Checks

- LED failure: **PASS**
- API timeout: **PASS**

### Capture Verdict

**Result:** **FAIL**

**Reason:** expected 10 images, observed 3; capture duration 17.06s exceeded application deadline 0.00s

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #33

**Start time:** `2026-05-27 18:15:10.821`

**Device detected:** `2026-05-27 18:15:28.060`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (0s): **FAIL**
  - Observed duration: 9.58s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.27s

> Note: the log does not contain an explicit electrical power-on timestamp. Device detection is therefore used as an observable proxy.

### Raw Image Validation

- Raw saving enabled: **PASS**
- Raw Left files observed: 0
- Raw Right files observed: 0
- Raw stereo-pair evidence: **NOT VERIFIED**

### Processed Image Validation

- Processed saving enabled: **PASS**
- Processed Left files observed: 0
- Processed Right files observed: 0
- Processed stereo-pair evidence: **NOT VERIFIED**

### Error Checks

- LED failure: **PASS**
- API timeout: **PASS**

### Capture Verdict

**Result:** **FAIL**

**Reason:** capture duration 9.58s exceeded application deadline 0.00s

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #34

**Start time:** `2026-05-27 18:19:11.430`

**Device detected:** `2026-05-27 18:19:27.497`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (0s): **FAIL**
  - Observed duration: 9.39s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 12.81s

> Note: the log does not contain an explicit electrical power-on timestamp. Device detection is therefore used as an observable proxy.

### Raw Image Validation

- Raw saving enabled: **PASS**
- Raw Left files observed: 0
- Raw Right files observed: 0
- Raw stereo-pair evidence: **NOT VERIFIED**

### Processed Image Validation

- Processed saving enabled: **PASS**
- Processed Left files observed: 0
- Processed Right files observed: 0
- Processed stereo-pair evidence: **NOT VERIFIED**

### Error Checks

- LED failure: **PASS**
- API timeout: **PASS**

### Capture Verdict

**Result:** **FAIL**

**Reason:** capture duration 9.39s exceeded application deadline 0.00s

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #35

**Start time:** `2026-05-27 18:23:11.694`

**Device detected:** `2026-05-27 18:23:28.023`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (0s): **FAIL**
  - Observed duration: 9.88s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.47s

> Note: the log does not contain an explicit electrical power-on timestamp. Device detection is therefore used as an observable proxy.

### Raw Image Validation

- Raw saving enabled: **PASS**
- Raw Left files observed: 0
- Raw Right files observed: 0
- Raw stereo-pair evidence: **NOT VERIFIED**

### Processed Image Validation

- Processed saving enabled: **PASS**
- Processed Left files observed: 0
- Processed Right files observed: 0
- Processed stereo-pair evidence: **NOT VERIFIED**

### Error Checks

- LED failure: **PASS**
- API timeout: **PASS**

### Capture Verdict

**Result:** **FAIL**

**Reason:** capture duration 9.88s exceeded application deadline 0.00s

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #36

**Start time:** `2026-05-27 18:27:13.358`

**Device detected:** `2026-05-27 18:27:29.983`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (0s): **FAIL**
  - Observed duration: 9.88s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.37s

> Note: the log does not contain an explicit electrical power-on timestamp. Device detection is therefore used as an observable proxy.

### Raw Image Validation

- Raw saving enabled: **PASS**
- Raw Left files observed: 0
- Raw Right files observed: 0
- Raw stereo-pair evidence: **NOT VERIFIED**

### Processed Image Validation

- Processed saving enabled: **PASS**
- Processed Left files observed: 0
- Processed Right files observed: 0
- Processed stereo-pair evidence: **NOT VERIFIED**

### Error Checks

- LED failure: **PASS**
- API timeout: **PASS**

### Capture Verdict

**Result:** **FAIL**

**Reason:** capture duration 9.88s exceeded application deadline 0.00s

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #37

**Start time:** `2026-05-27 18:31:11.222`

**Device detected:** `2026-05-27 18:31:28.370`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (0s): **FAIL**
  - Observed duration: 9.88s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.95s

> Note: the log does not contain an explicit electrical power-on timestamp. Device detection is therefore used as an observable proxy.

### Raw Image Validation

- Raw saving enabled: **PASS**
- Raw Left files observed: 0
- Raw Right files observed: 0
- Raw stereo-pair evidence: **NOT VERIFIED**

### Processed Image Validation

- Processed saving enabled: **PASS**
- Processed Left files observed: 0
- Processed Right files observed: 0
- Processed stereo-pair evidence: **NOT VERIFIED**

### Error Checks

- LED failure: **PASS**
- API timeout: **PASS**

### Capture Verdict

**Result:** **FAIL**

**Reason:** capture duration 9.88s exceeded application deadline 0.00s

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #38

**Start time:** `2026-05-27 18:35:12.949`

**Device detected:** `2026-05-27 18:35:29.045`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (0s): **FAIL**
  - Observed duration: 9.49s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.21s

> Note: the log does not contain an explicit electrical power-on timestamp. Device detection is therefore used as an observable proxy.

### Raw Image Validation

- Raw saving enabled: **PASS**
- Raw Left files observed: 0
- Raw Right files observed: 0
- Raw stereo-pair evidence: **NOT VERIFIED**

### Processed Image Validation

- Processed saving enabled: **PASS**
- Processed Left files observed: 0
- Processed Right files observed: 0
- Processed stereo-pair evidence: **NOT VERIFIED**

### Error Checks

- LED failure: **PASS**
- API timeout: **PASS**

### Capture Verdict

**Result:** **FAIL**

**Reason:** capture duration 9.49s exceeded application deadline 0.00s

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #39

**Start time:** `2026-05-27 18:39:13.217`

**Device detected:** `2026-05-27 18:39:30.078`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (0s): **FAIL**
  - Observed duration: 9.98s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 14.17s

> Note: the log does not contain an explicit electrical power-on timestamp. Device detection is therefore used as an observable proxy.

### Raw Image Validation

- Raw saving enabled: **PASS**
- Raw Left files observed: 0
- Raw Right files observed: 0
- Raw stereo-pair evidence: **NOT VERIFIED**

### Processed Image Validation

- Processed saving enabled: **PASS**
- Processed Left files observed: 0
- Processed Right files observed: 0
- Processed stereo-pair evidence: **NOT VERIFIED**

### Error Checks

- LED failure: **PASS**
- API timeout: **PASS**

### Capture Verdict

**Result:** **FAIL**

**Reason:** capture duration 9.98s exceeded application deadline 0.00s

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #40

**Start time:** `2026-05-27 18:43:12.435`

**Device detected:** `2026-05-27 18:43:28.727`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (0s): **FAIL**
  - Observed duration: 10.18s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.68s

> Note: the log does not contain an explicit electrical power-on timestamp. Device detection is therefore used as an observable proxy.

### Raw Image Validation

- Raw saving enabled: **PASS**
- Raw Left files observed: 0
- Raw Right files observed: 0
- Raw stereo-pair evidence: **NOT VERIFIED**

### Processed Image Validation

- Processed saving enabled: **PASS**
- Processed Left files observed: 0
- Processed Right files observed: 0
- Processed stereo-pair evidence: **NOT VERIFIED**

### Error Checks

- LED failure: **PASS**
- API timeout: **PASS**

### Capture Verdict

**Result:** **FAIL**

**Reason:** capture duration 10.18s exceeded application deadline 0.00s

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #41

**Start time:** `2026-05-27 18:47:13.246`

**Device detected:** `2026-05-27 18:47:29.616`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (0s): **FAIL**
  - Observed duration: 10.08s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.72s

> Note: the log does not contain an explicit electrical power-on timestamp. Device detection is therefore used as an observable proxy.

### Raw Image Validation

- Raw saving enabled: **PASS**
- Raw Left files observed: 0
- Raw Right files observed: 0
- Raw stereo-pair evidence: **NOT VERIFIED**

### Processed Image Validation

- Processed saving enabled: **PASS**
- Processed Left files observed: 0
- Processed Right files observed: 0
- Processed stereo-pair evidence: **NOT VERIFIED**

### Error Checks

- LED failure: **PASS**
- API timeout: **PASS**

### Capture Verdict

**Result:** **FAIL**

**Reason:** capture duration 10.08s exceeded application deadline 0.00s

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #42

**Start time:** `2026-05-27 18:51:14.312`

**Device detected:** `2026-05-27 18:51:30.861`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (0s): **FAIL**
  - Observed duration: 9.98s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.46s

> Note: the log does not contain an explicit electrical power-on timestamp. Device detection is therefore used as an observable proxy.

### Raw Image Validation

- Raw saving enabled: **PASS**
- Raw Left files observed: 0
- Raw Right files observed: 0
- Raw stereo-pair evidence: **NOT VERIFIED**

### Processed Image Validation

- Processed saving enabled: **PASS**
- Processed Left files observed: 0
- Processed Right files observed: 0
- Processed stereo-pair evidence: **NOT VERIFIED**

### Error Checks

- LED failure: **PASS**
- API timeout: **PASS**

### Capture Verdict

**Result:** **FAIL**

**Reason:** capture duration 9.98s exceeded application deadline 0.00s

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #43

**Start time:** `2026-05-27 18:55:13.282`

**Device detected:** `2026-05-27 18:55:29.762`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (0s): **FAIL**
  - Observed duration: 9.98s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.66s

> Note: the log does not contain an explicit electrical power-on timestamp. Device detection is therefore used as an observable proxy.

### Raw Image Validation

- Raw saving enabled: **PASS**
- Raw Left files observed: 0
- Raw Right files observed: 0
- Raw stereo-pair evidence: **NOT VERIFIED**

### Processed Image Validation

- Processed saving enabled: **PASS**
- Processed Left files observed: 0
- Processed Right files observed: 0
- Processed stereo-pair evidence: **NOT VERIFIED**

### Error Checks

- LED failure: **PASS**
- API timeout: **PASS**

### Capture Verdict

**Result:** **FAIL**

**Reason:** capture duration 9.98s exceeded application deadline 0.00s

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #44

**Start time:** `2026-05-27 18:59:13.383`

**Device detected:** `2026-05-27 18:59:29.915`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (0s): **FAIL**
  - Observed duration: 9.78s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.40s

> Note: the log does not contain an explicit electrical power-on timestamp. Device detection is therefore used as an observable proxy.

### Raw Image Validation

- Raw saving enabled: **PASS**
- Raw Left files observed: 0
- Raw Right files observed: 0
- Raw stereo-pair evidence: **NOT VERIFIED**

### Processed Image Validation

- Processed saving enabled: **PASS**
- Processed Left files observed: 0
- Processed Right files observed: 0
- Processed stereo-pair evidence: **NOT VERIFIED**

### Error Checks

- LED failure: **PASS**
- API timeout: **PASS**

### Capture Verdict

**Result:** **FAIL**

**Reason:** capture duration 9.78s exceeded application deadline 0.00s

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #45

**Start time:** `2026-05-27 19:03:13.168`

**Device detected:** `2026-05-27 19:03:29.918`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (0s): **FAIL**
  - Observed duration: 10.18s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.54s

> Note: the log does not contain an explicit electrical power-on timestamp. Device detection is therefore used as an observable proxy.

### Raw Image Validation

- Raw saving enabled: **PASS**
- Raw Left files observed: 0
- Raw Right files observed: 0
- Raw stereo-pair evidence: **NOT VERIFIED**

### Processed Image Validation

- Processed saving enabled: **PASS**
- Processed Left files observed: 0
- Processed Right files observed: 0
- Processed stereo-pair evidence: **NOT VERIFIED**

### Error Checks

- LED failure: **PASS**
- API timeout: **PASS**

### Capture Verdict

**Result:** **FAIL**

**Reason:** capture duration 10.18s exceeded application deadline 0.00s

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #46

**Start time:** `2026-05-27 19:07:11.914`

**Device detected:** `2026-05-27 19:07:28.842`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (0s): **FAIL**
  - Observed duration: 10.18s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 14.49s

> Note: the log does not contain an explicit electrical power-on timestamp. Device detection is therefore used as an observable proxy.

### Raw Image Validation

- Raw saving enabled: **PASS**
- Raw Left files observed: 0
- Raw Right files observed: 0
- Raw stereo-pair evidence: **NOT VERIFIED**

### Processed Image Validation

- Processed saving enabled: **PASS**
- Processed Left files observed: 0
- Processed Right files observed: 0
- Processed stereo-pair evidence: **NOT VERIFIED**

### Error Checks

- LED failure: **PASS**
- API timeout: **PASS**

### Capture Verdict

**Result:** **FAIL**

**Reason:** capture duration 10.18s exceeded application deadline 0.00s

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #47

**Start time:** `2026-05-27 19:11:12.178`

**Device detected:** `2026-05-27 19:11:28.687`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (0s): **FAIL**
  - Observed duration: 9.28s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 12.67s

> Note: the log does not contain an explicit electrical power-on timestamp. Device detection is therefore used as an observable proxy.

### Raw Image Validation

- Raw saving enabled: **PASS**
- Raw Left files observed: 0
- Raw Right files observed: 0
- Raw stereo-pair evidence: **NOT VERIFIED**

### Processed Image Validation

- Processed saving enabled: **PASS**
- Processed Left files observed: 0
- Processed Right files observed: 0
- Processed stereo-pair evidence: **NOT VERIFIED**

### Error Checks

- LED failure: **PASS**
- API timeout: **PASS**

### Capture Verdict

**Result:** **FAIL**

**Reason:** capture duration 9.28s exceeded application deadline 0.00s

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #48

**Start time:** `2026-05-27 19:15:14.462`

**Device detected:** `2026-05-27 19:15:31.028`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (0s): **FAIL**
  - Observed duration: 9.77s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.35s

> Note: the log does not contain an explicit electrical power-on timestamp. Device detection is therefore used as an observable proxy.

### Raw Image Validation

- Raw saving enabled: **PASS**
- Raw Left files observed: 0
- Raw Right files observed: 0
- Raw stereo-pair evidence: **NOT VERIFIED**

### Processed Image Validation

- Processed saving enabled: **PASS**
- Processed Left files observed: 0
- Processed Right files observed: 0
- Processed stereo-pair evidence: **NOT VERIFIED**

### Error Checks

- LED failure: **PASS**
- API timeout: **PASS**

### Capture Verdict

**Result:** **FAIL**

**Reason:** capture duration 9.77s exceeded application deadline 0.00s

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #49

**Start time:** `2026-05-27 19:19:13.196`

**Device detected:** `2026-05-27 19:19:29.963`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (0s): **FAIL**
  - Observed duration: 10.09s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.45s

> Note: the log does not contain an explicit electrical power-on timestamp. Device detection is therefore used as an observable proxy.

### Raw Image Validation

- Raw saving enabled: **PASS**
- Raw Left files observed: 0
- Raw Right files observed: 0
- Raw stereo-pair evidence: **NOT VERIFIED**

### Processed Image Validation

- Processed saving enabled: **PASS**
- Processed Left files observed: 0
- Processed Right files observed: 0
- Processed stereo-pair evidence: **NOT VERIFIED**

### Error Checks

- LED failure: **PASS**
- API timeout: **PASS**

### Capture Verdict

**Result:** **FAIL**

**Reason:** capture duration 10.09s exceeded application deadline 0.00s

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #50

**Start time:** `2026-05-27 19:23:12.057`

**Device detected:** `2026-05-27 19:23:28.593`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (0s): **FAIL**
  - Observed duration: 9.48s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.72s

> Note: the log does not contain an explicit electrical power-on timestamp. Device detection is therefore used as an observable proxy.

### Raw Image Validation

- Raw saving enabled: **PASS**
- Raw Left files observed: 0
- Raw Right files observed: 0
- Raw stereo-pair evidence: **NOT VERIFIED**

### Processed Image Validation

- Processed saving enabled: **PASS**
- Processed Left files observed: 0
- Processed Right files observed: 0
- Processed stereo-pair evidence: **NOT VERIFIED**

### Error Checks

- LED failure: **PASS**
- API timeout: **PASS**

### Capture Verdict

**Result:** **FAIL**

**Reason:** capture duration 9.48s exceeded application deadline 0.00s

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #51

**Start time:** `2026-05-27 19:27:13.474`

**Device detected:** `2026-05-27 19:27:30.401`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (0s): **FAIL**
  - Observed duration: 9.28s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 12.97s

> Note: the log does not contain an explicit electrical power-on timestamp. Device detection is therefore used as an observable proxy.

### Raw Image Validation

- Raw saving enabled: **PASS**
- Raw Left files observed: 0
- Raw Right files observed: 0
- Raw stereo-pair evidence: **NOT VERIFIED**

### Processed Image Validation

- Processed saving enabled: **PASS**
- Processed Left files observed: 0
- Processed Right files observed: 0
- Processed stereo-pair evidence: **NOT VERIFIED**

### Error Checks

- LED failure: **PASS**
- API timeout: **PASS**

### Capture Verdict

**Result:** **FAIL**

**Reason:** capture duration 9.28s exceeded application deadline 0.00s

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Overall Assessment

- PASS sessions: 0
- FAIL sessions: 48
- INCOMPLETE sessions: 3
- Overall result: **FAIL**
