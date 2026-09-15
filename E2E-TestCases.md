### **E2E-001: Camera Synchronization** 

#### Test Case: Physical Camera Synchronization

| Item | Description |
| ----- | ----- |
| **Test ID** | CAM-SYNC-001 |
| **Objective** | Verify that Camera 1 and Camera 2 capture the same scene at the same time within the required synchronization tolerance. |
| **Setup** | NVIDIA Jetson SBC, two MIPI/CSI-2 cameras, STM32F405 trigger/strobe controller, and a **rotating optical target** with a **sinusoidal wave pattern**. |
| **Stimulus** | The STM32 generates synchronized camera trigger/strobe signals while the optical target rotates at a controlled speed. |
| **Procedure** | 1\. Start the optical target at a defined rotational speed. 2\. Generate synchronized camera trigger/strobe signals from the STM32. 3\. Capture frames from both cameras. 4\. Use Python/OpenCV to extract the sinusoidal wave pattern from each image. 5\. **Measure the phase of the sinusoidal wave in each image.** 6\. Calculate the phase difference between the two cameras. 7\. Convert the phase difference to an estimated time difference using the known rotational speed. 8\. Repeat the test over multiple captures and operating conditions. |
| **Expected Result** | Both cameras observe the sinusoidal wave pattern at the same phase, within the specified synchronization tolerance. |
| **Pass Criteria** | The calculated camera synchronization error is within the specified requirement (for example, ≤ 1 µs), with no unexpected dropped or corrupted frames. |
| **Automation** | **High.** Python/OpenCV can automatically extract the sinusoidal wave pattern, calculate phase difference, estimate synchronization error, and generate a PASS/FAIL result. |
| **Additional Equipment** | A controlled rotating optical target is required. An oscilloscope or logic analyzer is recommended to independently verify the electrical timing of the MCU trigger/strobe signals. |
| **Limitation** | Image analysis alone cannot conclusively prove 1 µs electrical timing accuracy. Camera exposure timing, sensor characteristics, mechanical speed variation, and image-processing accuracy must also be considered. |
| **Assumptions** | • The rotating target speed shall be controlled within a defined range.<br>• The maximum rotation speed shall ensure that target motion during camera exposure does not introduce unacceptable motion blur.<br>• Because exposure may be configured automatically, the test shall either use a controlled/fixed exposure time or verify the actual exposure time before determining the maximum allowable rotation speed.<br>• The minimum rotation speed shall provide sufficient phase change to detect the specified camera synchronization error. |

#### Test Case: Camera Frame Timestamp Matching

| Item | Description |
| ----- | ----- |
| **Test ID** | CAM-MATCH-001 |
| **Objective** | Verify that the software identifies and handles timestamp differences between Camera 1 and Camera 2 frames that exceed the required synchronization tolerance. |
| **Setup** | NVIDIA Jetson SBC, two MIPI/CSI-2 cameras, StereoCamera software, and system logging enabled. |
| **Stimulus** | Camera 1 and Camera 2 generate image frames during normal stereo-camera operation. |
| **Procedure** | 1\. Start the stereo camera system. 2\. Allow Camera 1 and Camera 2 to generate image frames. 3\. Monitor the StereoCamera application logs for frame-matching information. 4\. Extract the timestamp difference reported between the left and right camera frames. 5\. Compare the reported difference against the configured synchronization tolerance. 6\. Verify that the software handles an excessive timestamp difference according to the defined frame-matching policy. 7\. Repeat the test over multiple captures and operating conditions. |
| **Expected Result** | The software correctly identifies frame pairs whose timestamp difference exceeds the configured synchronization tolerance and handles the mismatch according to the defined frame-matching policy. |
| **Pass Criteria** | The reported frame timestamp difference is within the specified synchronization tolerance during normal operation. When the tolerance is exceeded, the software correctly rejects or drops the invalid frame pair and generates an appropriate diagnostic message. |
| **Automation** | **High.** Python can parse the application logs, extract frame timestamp differences, compare them against the configured limit, verify the expected frame-drop behavior, and generate a PASS/FAIL result. |
| **Additional Equipment** | No additional equipment is required for log-based validation. A logic analyzer or oscilloscope is recommended for independently verifying the physical timing of the MCU trigger/strobe signals. |
| **Limitation** | This test validates **application-level frame timestamp matching**. It does not conclusively prove the physical timing of camera exposure or the electrical timing of the MCU trigger/strobe signals. |
| **Assumptions** | The StereoCamera software logs the timestamp difference between Camera 1 and Camera 2 frames and defines the expected behavior when the synchronization tolerance is exceeded. |
| **Observed Result** | `ImageMatching: diff=500006us dropping left` |
| **Test Result** | **FAIL** — The observed frame timestamp difference was approximately **500 ms**, exceeding the example synchronization limit of **1 ms (1,000 µs)**. |

### **E2E-002: Remote Control → MCU → Camera Capture → Telemetry**

| Item | Description |
| ----- | ----- |
| **Test ID** | E2E-002 |
| **Objective** | Verify that a remote command can travel through the complete system and successfully trigger camera acquisition and return status. |
| **System Path** | Remote PC → Gigabit Ethernet → Jetson → UART → STM32F405 → GPIO trigger/strobe → Cameras → Jetson → Ethernet → Remote PC |
| **Stimulus** | Send a camera-capture command from a remote PC over Ethernet. |
| **Procedure** | 1\. Connect the Jetson to the test network. 2\. Start the camera and MCU services. 3\. Send a capture command from the remote PC. 4\. Verify the Jetson receives and processes the command. 5\. Verify the command is transmitted to the STM32 over UART. 6\. Verify the STM32 generates the expected camera trigger/strobe signals. 7\. Verify both cameras capture frames. 8\. Verify capture status/telemetry is returned to the remote PC. |
| **Expected Result** | The remote command results in a successful synchronized camera capture, and the correct status is returned to the remote system. |
| **Pass Criteria** | Command is received, processed, and acknowledged without timeout or communication error; expected camera frames are produced; returned telemetry indicates successful capture. |
| **Automation** | **High.** Python can send commands, monitor telemetry, verify UART messages, check captured frames, and generate PASS/FAIL results. |
| **Key Failure Modes** | Ethernet communication failure, invalid command handling, UART communication error, missing trigger, camera capture failure, timeout, incorrect telemetry. |

**Assumptions:**

* The Jetson provides a defined remote-control interface over Gigabit Ethernet, such as an API or command interface.  
* The Jetson has a documented UART protocol for communicating with the STM32F405.  
* The STM32 firmware supports the required camera trigger/strobe command and reports capture status.  
* Both cameras are configured and operational before the E2E test begins.  
* The system provides sufficient telemetry or logging to determine whether each stage of the command path succeeded.  
* The required network, UART, and camera interfaces are available and accessible in the open-system test configuration.

### **E2E-003: OTA Firmware Update and CRC Fault Injection**

| Item | Description |
| ----- | ----- |
| **Test ID** | E2E-003 |
| **Objective** | Verify that the OTA firmware update process successfully installs a valid firmware image and safely rejects a corrupted image detected through CRC verification. |
| **System Path** | Remote PC → Gigabit Ethernet → Jetson → UART/Boot Interface → STM32F405 → Reboot → Jetson → Ethernet Telemetry |
| **Normal Stimulus** | Initiate an OTA firmware update using a known-good firmware image. |
| **Fault Stimulus** | Intentionally modify the firmware image or its CRC value before/during the update so that the received image fails CRC verification. |
| **Normal Procedure** | 1\. Record the current MCU firmware version. 2\. Transfer the valid firmware image to the Jetson. 3\. Initiate the OTA update remotely. 4\. Transfer the firmware to the STM32. 5\. Verify CRC and update completion. 6\. Reboot the STM32. 7\. Verify the new firmware version. 8\. Verify normal MCU-to-Jetson communication and camera functionality. |
| **Fault-Injection Procedure** | 1\. Prepare a known-good firmware image. 2\. Introduce a controlled data corruption that causes a CRC mismatch. 3\. Initiate the OTA update using the corrupted image. 4\. Verify that the update process detects the CRC error. 5\. Verify that the corrupted firmware is rejected and is not activated. 6\. Verify that the system reports an appropriate error/status. 7\. Reboot/recover the system according to the defined update procedure. 8\. Verify that the previously known-good firmware or other safe recovery mechanism remains functional. |
| **Expected Result – Normal** | The valid firmware passes CRC verification, is installed successfully, and the MCU boots with the expected firmware version. |
| **Expected Result – Fault** | The corrupted firmware fails CRC verification and is rejected. The MCU does not activate the invalid image and the system reports the update failure. |
| **Pass Criteria – Normal** | Firmware version matches the expected version; MCU communication is restored; camera functionality remains operational. |
| **Pass Criteria – Fault** | CRC error is detected; corrupted firmware is not activated; an appropriate error is reported; the system remains recoverable and returns to a known-good state. |
| **Automation** | **High.** The test framework can calculate/modify the test image, initiate OTA, monitor update status, verify CRC failure, check firmware version, and validate system recovery. |
| **Key Failure Modes** | Corrupted image accepted, CRC mismatch not detected, invalid firmware activated, MCU fails to boot, incorrect error reporting, loss of recovery path. |
| **Assumptions** | The OTA protocol includes CRC or equivalent integrity verification and defines expected behavior when verification fails. A recovery or rollback mechanism is available by the product design. |

