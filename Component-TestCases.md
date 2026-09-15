

| Category | Test Cases  |
| ----- | ----- |
| **SBC** | SBC-001 Linux health, SBC-002 CSI-2 interface |
| **MCU** | MCU-001 UART, MCU-002 GPIO/boot/reset, MCU-003 Heartbeat Monitoring |
| **Cameras** | CAM-001 individual acquisition, CAM-002 synchronization |
| **Storage** | SSD-001 performance/integrity, SSD-002 sustained recording |
| **Network** | NET-001 connectivity/throughput, NET-002 stress/recovery |
| **E2E** | E2E-001 camera synchronization, E2E-002 remote capture, E2E-003 OTA \+ CRC fault injection |

**Total: 11 component tests \+ 3 E2E scenarios.**

## **Component-Level Test Cases**

### **1\. SBC — NVIDIA Jetson**

#### **SBC-001: Linux System Health and Resource Stability**

| Item | Description |
| ----- | ----- |
| **Objective** | Verify that the Jetson Linux system boots correctly and remains stable under normal system load. |
| **Procedure** | Boot the Jetson and verify CPU, memory, storage, USB, CSI-2, network interfaces, kernel logs, and system services. Run a sustained workload and monitor system resources. |
| **Expected Result** | System boots without errors, all required interfaces are detected, and the system remains stable without unexpected crashes, kernel errors, or resource exhaustion. |
| **Pass Criteria** | No critical kernel/system errors; required hardware is detected; CPU/memory usage remains within defined limits; system remains responsive. |
| **Automation** | **High** — Linux scripts can collect `dmesg`, `/proc`, `/sys`, device information, and resource statistics. |

#### **SBC-002: CSI-2 Camera Interface**

| Item | Description |
| ----- | ----- |
| **Objective** | Verify that the Jetson can correctly initialize and acquire image streams from both CSI-2 cameras. |
| **Procedure** | Connect Camera 1 and Camera 2, configure the expected resolution/frame rate, start acquisition, and capture a defined number of frames. Monitor for CSI-2 errors and dropped frames. |
| **Expected Result** | Both cameras initialize successfully and continuously deliver frames at the configured parameters. |
| **Pass Criteria** | Expected resolution/frame rate achieved; no unexpected CSI-2 errors; no unexplained frame drops or corrupted frames. |
| **Automation** | **High** — v412-ctl and Python can automate acquisition and frame validation. |

---

### **2\. MCU — STM32F405**

#### **MCU-001: UART Communication**

| Item | Description |
| ----- | ----- |
| **Objective** | Verify reliable bidirectional communication between the Jetson and STM32F405 over UART. |
| **Procedure** | Send defined commands from the Jetson to the MCU and verify responses. Test normal commands, invalid commands, repeated commands, and communication timeouts. |
| **Expected Result** | Valid commands receive the correct response and invalid commands are handled according to the protocol. |
| **Pass Criteria** | No unexpected communication errors; messages are correctly received, parsed, and acknowledged; timeout/error handling works as specified. |
| **Automation** | **High** — Python can send commands and validate responses. |

#### **MCU-002: GPIO Boot/Reset and IPC Control**

| Item | Description |
| ----- | ----- |
| **Objective** | Verify that the Jetson can correctly control the STM32F405 through BOOT0, RESET, and IPC GPIO signals. |
| **Procedure** | Exercise the defined boot and reset sequences and verify MCU startup behavior. Verify IPC GPIO signaling during normal operation. |
| **Expected Result** | The MCU enters the expected boot/normal mode and responds correctly to reset and IPC signals. |
| **Pass Criteria** | MCU consistently enters the expected state; reset behavior is deterministic; IPC signals are detected and handled correctly. |
| **Automation** | **Partial/High** — software can control and verify GPIO states; an oscilloscope/logic analyzer may be required to verify precise electrical timing. |

### **MCU-003: MCU Heartbeat Monitoring**

| Item | Description |
| ----- | ----- |
| **Test ID** | MCU-003 |
| **Objective** | Verify that the STM32F405 continuously provides a heartbeat indicating that the MCU firmware is running and communicating correctly with the Jetson. |
| **Procedure** | 1\. Start the STM32F405 and Jetson. 2\. Establish normal UART communication. 3\. Monitor the MCU heartbeat for a defined period. 4\. Verify heartbeat frequency and expected message/content. 5\. Introduce a controlled MCU reset and verify that the heartbeat stops and resumes after the MCU restarts. |
| **Expected Result** | The MCU produces a heartbeat at the expected interval during normal operation. After a reset, the heartbeat stops and resumes once the MCU has successfully restarted. |
| **Pass Criteria** | Heartbeat is received within the specified interval with no unexpected gaps; heartbeat contains the expected status information; MCU restart is detected and normal heartbeat resumes within the specified recovery time. |
| **Automation** | **High** — Python can monitor UART heartbeat messages, measure intervals, detect missed heartbeats, and generate PASS/FAIL results. |
| **Fault Coverage** | Detects MCU hang, firmware crash, UART communication failure, unexpected reset, or loss of MCU responsiveness. |
| **Assumptions** | The STM32 firmware provides a defined heartbeat mechanism and the expected heartbeat interval/timeout is specified. |

---

### **3\. Camera 1 & Camera 2 — MIPI/CSI-2**

#### **CAM-001: Individual Camera Image Acquisition**

| Item | Description |
| ----- | ----- |
| **Objective** | Verify that each camera independently produces valid images through its CSI-2 interface. |
| **Procedure** | Test Camera 1 and Camera 2 independently at the required resolution and frame rate. Capture a defined number of frames and analyze image integrity. |
| **Expected Result** | Each camera produces valid frames without unexpected corruption or loss. |
| **Pass Criteria** | Correct resolution/frame rate; expected image format; no persistent corrupted frames; frame-drop rate within requirement. |
| **Automation** | **High** — automated frame capture and image-quality/integrity checks using Python/OpenCV. |

#### **CAM-002: Dual-Camera Synchronization**

This is your **sinusoidal wave pattern** test.

| Item | Description |
| ----- | ----- |
| **Objective** | Verify that both cameras capture the same scene at the same time within the required synchronization tolerance. |
| **Procedure** | Use the STM32 to generate synchronized trigger/strobe signals while a rotating optical target with a sinusoidal wave pattern is observed by both cameras. Use Python/OpenCV to measure the sinusoidal phase in each image and calculate the corresponding timing difference. |
| **Expected Result** | Both cameras observe the sinusoidal wave at the same phase within the specified synchronization tolerance. |
| **Pass Criteria** | Calculated synchronization error is within the specified requirement, with no unexpected dropped or corrupted frames. |
| **Automation** | **High** — Python/OpenCV can perform phase analysis and automatically generate PASS/FAIL. |
| **Additional Equipment** | Oscilloscope or logic analyzer recommended for independent electrical timing verification. |

---

### **4\. Storage — External SSD**

#### **SSD-001: Read/Write Performance and Integrity**

| Item | Description |
| ----- | ----- |
| **Objective** | Verify that the USB 3.0 SSD provides sufficient performance for image/data storage. |
| **Procedure** | Perform sequential and random read/write tests using representative data sizes. |
| **Expected Result** | SSD achieves the required throughput without I/O errors. |
| **Pass Criteria** | Read/write performance meets the defined requirement; no I/O errors or unexpected disconnections. |
| **Automation** | **High** — `fio` can automate performance and integrity testing. |

#### **SSD-002: Sustained Image Recording**

| Item | Description |
| ----- | ----- |
| **Objective** | Verify that the SSD can continuously store camera data for the required operating period. |
| **Procedure** | Continuously record image data from the camera system to the SSD for the specified duration. Monitor storage throughput, disk space, I/O errors, and dropped frames. |
| **Expected Result** | Image data is continuously written without storage-related frame loss or corruption. |
| **Pass Criteria** | No unexpected I/O errors; required write throughput is maintained; recorded data can be read back successfully. |
| **Automation** | **High** — automated recording, disk monitoring, file validation, and log analysis. |

---

### **5\. Network — Gigabit Ethernet**

#### **NET-001: Ethernet Connectivity and Throughput**

| Item | Description |
| ----- | ----- |
| **Objective** | Verify reliable Gigabit Ethernet connectivity and sufficient network throughput. |
| **Procedure** | Establish an Ethernet connection and perform throughput, packet-loss, and interface-health tests. |
| **Expected Result** | Ethernet operates at the expected link speed with stable communication and sufficient throughput. |
| **Pass Criteria** | Link negotiates at 1 Gbps where supported; throughput meets requirement; no unexpected packet loss or interface errors. |
| **Automation** | **High** — `ethtool` and `iperf3` can automate link and throughput testing. |

#### **NET-002: Network Stress and Recovery**

| Item | Description |
| ----- | ----- |
| **Objective** | Verify that the system handles sustained network traffic and recovers correctly from a network interruption. |
| **Procedure** | Generate sustained Ethernet traffic while monitoring telemetry/control communication. Interrupt and restore the network connection, then verify system recovery. |
| **Expected Result** | Normal communication remains reliable under load and the system recovers correctly after network reconnection. |
| **Pass Criteria** | No system crash or data corruption; communication resumes within the specified recovery time; appropriate errors/status are reported. |
| **Automation** | **High** — traffic generation, monitoring, fault detection, and recovery verification can be scripted. |

