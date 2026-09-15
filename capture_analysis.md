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
| 2 | PASS | 10/10 | 9.88s | 13.98s |
| 3 | PASS | 10/10 | 9.69s | 13.48s |
| 4 | PASS | 10/10 | 10.18s | 13.62s |
| 5 | PASS | 10/10 | 10.09s | 14.28s |
| 6 | PASS | 10/10 | 10.08s | 14.04s |
| 7 | PASS | 10/10 | 10.18s | 14.17s |
| 8 | PASS | 10/10 | 9.88s | 13.36s |
| 9 | PASS | 10/10 | 9.98s | 13.84s |
| 10 | PASS | 10/10 | 10.38s | 13.78s |
| 11 | PASS | 10/10 | 9.66s | 13.96s |
| 12 | PASS | 10/10 | 9.98s | 14.27s |
| 13 | PASS | 10/10 | 10.08s | 13.54s |
| 14 | PASS | 10/10 | 9.38s | 13.12s |
| 15 | PASS | 10/10 | 10.18s | 13.54s |
| 16 | PASS | 10/10 | 9.99s | 13.63s |
| 17 | PASS | 10/10 | 9.19s | 12.60s |
| 18 | PASS | 10/10 | 9.88s | 13.25s |
| 19 | PASS | 10/10 | 10.38s | 14.60s |
| 20 | INCOMPLETE | N/A | N/A | N/A |
| 21 | FAIL | 22/10 | 21.61s | 24.96s |
| 22 | PASS | 10/10 | 9.78s | 13.63s |
| 23 | PASS | 10/10 | 9.98s | 14.14s |
| 24 | PASS | 10/10 | 9.58s | 13.60s |
| 25 | PASS | 10/10 | 9.68s | 13.22s |
| 26 | PASS | 10/10 | 9.98s | 13.44s |
| 27 | PASS | 10/10 | 10.08s | 13.43s |
| 28 | PASS | 10/10 | 9.87s | 13.68s |
| 29 | PASS | 10/10 | 10.08s | 13.45s |
| 30 | PASS | 10/10 | 9.29s | 13.47s |
| 31 | FAIL | 3/10 | 17.06s | 20.95s |
| 32 | PASS | 10/10 | 9.58s | 13.27s |
| 33 | PASS | 10/10 | 9.39s | 12.80s |
| 34 | PASS | 10/10 | 9.88s | 13.47s |
| 35 | PASS | 10/10 | 9.88s | 13.36s |
| 36 | PASS | 10/10 | 9.88s | 13.94s |
| 37 | PASS | 10/10 | 9.49s | 13.21s |
| 38 | PASS | 10/10 | 9.98s | 14.17s |
| 39 | PASS | 10/10 | 10.18s | 13.67s |
| 40 | PASS | 10/10 | 10.08s | 13.72s |
| 41 | PASS | 10/10 | 9.98s | 13.46s |
| 42 | PASS | 10/10 | 9.98s | 13.65s |
| 43 | PASS | 10/10 | 9.78s | 13.39s |
| 44 | PASS | 10/10 | 10.18s | 13.54s |
| 45 | PASS | 10/10 | 10.18s | 14.48s |
| 46 | PASS | 10/10 | 9.28s | 12.67s |
| 47 | PASS | 10/10 | 9.77s | 13.35s |
| 48 | PASS | 10/10 | 10.09s | 13.44s |
| 49 | PASS | 10/10 | 9.48s | 13.71s |
| 50 | PASS | 10/10 | 9.28s | 12.96s |

## Capture #1

**Start time:** `2026-05-27 16:07:30.213`

**Device detected:** `2026-05-27 16:07:26.665`

### Application-Level Validation

- Image count: **INCOMPLETE**
- Application deadline (15s): **NOT VERIFIED**

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

## Capture #2

**Start time:** `2026-05-27 16:11:31.499`

**Device detected:** `2026-05-27 16:11:27.396`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (15s): **PASS**
  - Observed duration: 9.88s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.98s

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

**Result:** **PASS**

**Reason:** All observed application checks passed.

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #3

**Start time:** `2026-05-27 16:15:29.612`

**Device detected:** `2026-05-27 16:15:25.824`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (15s): **PASS**
  - Observed duration: 9.69s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.48s

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

**Result:** **PASS**

**Reason:** All observed application checks passed.

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #4

**Start time:** `2026-05-27 16:19:30.228`

**Device detected:** `2026-05-27 16:19:26.786`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (15s): **PASS**
  - Observed duration: 10.18s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.62s

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

**Result:** **PASS**

**Reason:** All observed application checks passed.

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #5

**Start time:** `2026-05-27 16:23:30.213`

**Device detected:** `2026-05-27 16:23:26.023`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (15s): **PASS**
  - Observed duration: 10.09s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 14.28s

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

**Result:** **PASS**

**Reason:** All observed application checks passed.

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #6

**Start time:** `2026-05-27 16:27:32.185`

**Device detected:** `2026-05-27 16:27:28.228`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (15s): **PASS**
  - Observed duration: 10.08s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 14.04s

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

**Result:** **PASS**

**Reason:** All observed application checks passed.

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #7

**Start time:** `2026-05-27 16:31:32.128`

**Device detected:** `2026-05-27 16:31:28.144`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (15s): **PASS**
  - Observed duration: 10.18s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 14.17s

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

**Result:** **PASS**

**Reason:** All observed application checks passed.

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #8

**Start time:** `2026-05-27 16:35:31.411`

**Device detected:** `2026-05-27 16:35:27.938`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (15s): **PASS**
  - Observed duration: 9.88s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.36s

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

**Result:** **PASS**

**Reason:** All observed application checks passed.

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #9

**Start time:** `2026-05-27 16:39:30.336`

**Device detected:** `2026-05-27 16:39:26.478`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (15s): **PASS**
  - Observed duration: 9.98s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.84s

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

**Result:** **PASS**

**Reason:** All observed application checks passed.

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #10

**Start time:** `2026-05-27 16:43:29.219`

**Device detected:** `2026-05-27 16:43:25.819`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (15s): **PASS**
  - Observed duration: 10.38s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.78s

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

**Result:** **PASS**

**Reason:** All observed application checks passed.

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #11

**Start time:** `2026-05-27 16:47:31.733`

**Device detected:** `2026-05-27 16:47:27.432`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (15s): **PASS**
  - Observed duration: 9.66s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.96s

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

**Result:** **PASS**

**Reason:** All observed application checks passed.

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #12

**Start time:** `2026-05-27 16:51:30.479`

**Device detected:** `2026-05-27 16:51:26.191`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (15s): **PASS**
  - Observed duration: 9.98s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 14.27s

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

**Result:** **PASS**

**Reason:** All observed application checks passed.

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #13

**Start time:** `2026-05-27 16:55:30.294`

**Device detected:** `2026-05-27 16:55:26.836`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (15s): **PASS**
  - Observed duration: 10.08s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.54s

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

**Result:** **PASS**

**Reason:** All observed application checks passed.

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #14

**Start time:** `2026-05-27 16:59:30.973`

**Device detected:** `2026-05-27 16:59:27.232`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (15s): **PASS**
  - Observed duration: 9.38s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.12s

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

**Result:** **PASS**

**Reason:** All observed application checks passed.

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #15

**Start time:** `2026-05-27 17:03:29.311`

**Device detected:** `2026-05-27 17:03:25.953`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (15s): **PASS**
  - Observed duration: 10.18s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.54s

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

**Result:** **PASS**

**Reason:** All observed application checks passed.

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #16

**Start time:** `2026-05-27 17:07:29.484`

**Device detected:** `2026-05-27 17:07:25.845`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (15s): **PASS**
  - Observed duration: 9.99s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.63s

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

**Result:** **PASS**

**Reason:** All observed application checks passed.

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #17

**Start time:** `2026-05-27 17:11:29.108`

**Device detected:** `2026-05-27 17:11:25.692`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (15s): **PASS**
  - Observed duration: 9.19s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 12.60s

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

**Result:** **PASS**

**Reason:** All observed application checks passed.

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #18

**Start time:** `2026-05-27 17:15:29.383`

**Device detected:** `2026-05-27 17:15:26.013`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (15s): **PASS**
  - Observed duration: 9.88s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.25s

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

**Result:** **PASS**

**Reason:** All observed application checks passed.

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #19

**Start time:** `2026-05-27 17:19:29.161`

**Device detected:** `2026-05-27 17:19:24.949`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (15s): **PASS**
  - Observed duration: 10.38s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 14.60s

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

**Result:** **PASS**

**Reason:** All observed application checks passed.

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #20

**Start time:** `2026-05-27 17:23:29.357`

**Device detected:** `2026-05-27 17:23:25.349`

### Application-Level Validation

- Image count: **INCOMPLETE**
- Application deadline (15s): **NOT VERIFIED**

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

## Capture #21

**Start time:** `2026-05-27 17:31:29.088`

**Device detected:** `2026-05-27 17:31:25.741`

### Application-Level Validation

- Image count: **FAIL**
  - Expected: 10
  - Observed: 22
- Application deadline (15s): **FAIL**
  - Observed duration: 21.61s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 24.96s

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

- LED failure: **FAIL**
- API timeout: **FAIL**

### Capture Verdict

**Result:** **FAIL**

**Reason:** expected 10 images, observed 22; capture duration 21.61s exceeded application deadline 15.00s; LED disable failure detected; API timeout detected

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #22

**Start time:** `2026-05-27 17:35:28.467`

**Device detected:** `2026-05-27 17:35:24.618`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (15s): **PASS**
  - Observed duration: 9.78s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.63s

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

**Result:** **PASS**

**Reason:** All observed application checks passed.

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #23

**Start time:** `2026-05-27 17:39:29.285`

**Device detected:** `2026-05-27 17:39:25.130`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (15s): **PASS**
  - Observed duration: 9.98s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 14.14s

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

**Result:** **PASS**

**Reason:** All observed application checks passed.

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #24

**Start time:** `2026-05-27 17:43:28.779`

**Device detected:** `2026-05-27 17:43:24.759`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (15s): **PASS**
  - Observed duration: 9.58s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.60s

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

**Result:** **PASS**

**Reason:** All observed application checks passed.

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #25

**Start time:** `2026-05-27 17:47:29.841`

**Device detected:** `2026-05-27 17:47:26.300`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (15s): **PASS**
  - Observed duration: 9.68s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.22s

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

**Result:** **PASS**

**Reason:** All observed application checks passed.

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #26

**Start time:** `2026-05-27 17:51:29.389`

**Device detected:** `2026-05-27 17:51:25.929`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (15s): **PASS**
  - Observed duration: 9.98s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.44s

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

**Result:** **PASS**

**Reason:** All observed application checks passed.

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #27

**Start time:** `2026-05-27 17:55:30.287`

**Device detected:** `2026-05-27 17:55:26.943`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (15s): **PASS**
  - Observed duration: 10.08s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.43s

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

**Result:** **PASS**

**Reason:** All observed application checks passed.

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #28

**Start time:** `2026-05-27 17:59:30.590`

**Device detected:** `2026-05-27 17:59:26.786`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (15s): **PASS**
  - Observed duration: 9.87s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.68s

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

**Result:** **PASS**

**Reason:** All observed application checks passed.

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #29

**Start time:** `2026-05-27 18:03:29.423`

**Device detected:** `2026-05-27 18:03:26.059`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (15s): **PASS**
  - Observed duration: 10.08s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.45s

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

**Result:** **PASS**

**Reason:** All observed application checks passed.

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #30

**Start time:** `2026-05-27 18:07:31.096`

**Device detected:** `2026-05-27 18:07:26.909`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (15s): **PASS**
  - Observed duration: 9.29s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.47s

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

**Result:** **PASS**

**Reason:** All observed application checks passed.

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #31

**Start time:** `2026-05-27 18:11:31.342`

**Device detected:** `2026-05-27 18:11:27.444`

### Application-Level Validation

- Image count: **FAIL**
  - Expected: 10
  - Observed: 3
- Application deadline (15s): **FAIL**
  - Observed duration: 17.06s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 20.95s

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

**Result:** **FAIL**

**Reason:** expected 10 images, observed 3; capture duration 17.06s exceeded application deadline 15.00s

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #32

**Start time:** `2026-05-27 18:15:31.743`

**Device detected:** `2026-05-27 18:15:28.060`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (15s): **PASS**
  - Observed duration: 9.58s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.27s

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

**Result:** **PASS**

**Reason:** All observed application checks passed.

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #33

**Start time:** `2026-05-27 18:19:30.910`

**Device detected:** `2026-05-27 18:19:27.497`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (15s): **PASS**
  - Observed duration: 9.39s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 12.80s

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

**Result:** **PASS**

**Reason:** All observed application checks passed.

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #34

**Start time:** `2026-05-27 18:23:31.609`

**Device detected:** `2026-05-27 18:23:28.023`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (15s): **PASS**
  - Observed duration: 9.88s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.47s

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

**Result:** **PASS**

**Reason:** All observed application checks passed.

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #35

**Start time:** `2026-05-27 18:27:33.460`

**Device detected:** `2026-05-27 18:27:29.983`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (15s): **PASS**
  - Observed duration: 9.88s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.36s

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

**Result:** **PASS**

**Reason:** All observed application checks passed.

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #36

**Start time:** `2026-05-27 18:31:32.429`

**Device detected:** `2026-05-27 18:31:28.370`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (15s): **PASS**
  - Observed duration: 9.88s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.94s

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

**Result:** **PASS**

**Reason:** All observed application checks passed.

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #37

**Start time:** `2026-05-27 18:35:32.765`

**Device detected:** `2026-05-27 18:35:29.045`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (15s): **PASS**
  - Observed duration: 9.49s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.21s

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

**Result:** **PASS**

**Reason:** All observed application checks passed.

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #38

**Start time:** `2026-05-27 18:39:34.262`

**Device detected:** `2026-05-27 18:39:30.078`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (15s): **PASS**
  - Observed duration: 9.98s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 14.17s

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

**Result:** **PASS**

**Reason:** All observed application checks passed.

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #39

**Start time:** `2026-05-27 18:43:32.217`

**Device detected:** `2026-05-27 18:43:28.727`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (15s): **PASS**
  - Observed duration: 10.18s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.67s

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

**Result:** **PASS**

**Reason:** All observed application checks passed.

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #40

**Start time:** `2026-05-27 18:47:33.249`

**Device detected:** `2026-05-27 18:47:29.616`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (15s): **PASS**
  - Observed duration: 10.08s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.72s

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

**Result:** **PASS**

**Reason:** All observed application checks passed.

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #41

**Start time:** `2026-05-27 18:51:34.334`

**Device detected:** `2026-05-27 18:51:30.861`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (15s): **PASS**
  - Observed duration: 9.98s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.46s

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

**Result:** **PASS**

**Reason:** All observed application checks passed.

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #42

**Start time:** `2026-05-27 18:55:33.432`

**Device detected:** `2026-05-27 18:55:29.762`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (15s): **PASS**
  - Observed duration: 9.98s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.65s

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

**Result:** **PASS**

**Reason:** All observed application checks passed.

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #43

**Start time:** `2026-05-27 18:59:33.520`

**Device detected:** `2026-05-27 18:59:29.915`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (15s): **PASS**
  - Observed duration: 9.78s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.39s

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

**Result:** **PASS**

**Reason:** All observed application checks passed.

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #44

**Start time:** `2026-05-27 19:03:33.274`

**Device detected:** `2026-05-27 19:03:29.918`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (15s): **PASS**
  - Observed duration: 10.18s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.54s

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

**Result:** **PASS**

**Reason:** All observed application checks passed.

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #45

**Start time:** `2026-05-27 19:07:33.137`

**Device detected:** `2026-05-27 19:07:28.842`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (15s): **PASS**
  - Observed duration: 10.18s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 14.48s

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

**Result:** **PASS**

**Reason:** All observed application checks passed.

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #46

**Start time:** `2026-05-27 19:11:32.069`

**Device detected:** `2026-05-27 19:11:28.687`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (15s): **PASS**
  - Observed duration: 9.28s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 12.67s

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

**Result:** **PASS**

**Reason:** All observed application checks passed.

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #47

**Start time:** `2026-05-27 19:15:34.604`

**Device detected:** `2026-05-27 19:15:31.028`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (15s): **PASS**
  - Observed duration: 9.77s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.35s

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

**Result:** **PASS**

**Reason:** All observed application checks passed.

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #48

**Start time:** `2026-05-27 19:19:33.317`

**Device detected:** `2026-05-27 19:19:29.963`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (15s): **PASS**
  - Observed duration: 10.09s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.44s

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

**Result:** **PASS**

**Reason:** All observed application checks passed.

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #49

**Start time:** `2026-05-27 19:23:32.823`

**Device detected:** `2026-05-27 19:23:28.593`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (15s): **PASS**
  - Observed duration: 9.48s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 13.71s

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

**Result:** **PASS**

**Reason:** All observed application checks passed.

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Capture #50

**Start time:** `2026-05-27 19:27:34.081`

**Device detected:** `2026-05-27 19:27:30.401`

### Application-Level Validation

- Image count: **PASS**
  - Expected: 10
  - Observed: 10
- Application deadline (15s): **PASS**
  - Observed duration: 9.28s

### System-Level Validation

- 60-second requirement: **PASS**
  - Device detection → completion: 12.96s

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

**Result:** **PASS**

**Reason:** All observed application checks passed.

**Evidence limitation:** The application log does not provide enough correlated file-write evidence to prove the complete raw/processed stereo-pair requirement for this capture.

## Overall Assessment

- PASS sessions: 46
- FAIL sessions: 2
- INCOMPLETE sessions: 2
- Overall result: **FAIL**
