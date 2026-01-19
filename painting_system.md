# Software Requirements & System Architecture | Project ArmFlip

This document outlines the software ecosystem established by our team to ensure the seamless synchronization between the **UR3e collaborative robot** and our proposed **7th-axis rotary gantry** for the ArmFlip project (Workshop 2.1).

## 1. Technical Software Stack

We have selected the following tools to manage the complexity of the robotic integration:

| System Layer | Software / Tool | Team's Specific Implementation |
| :--- | :--- | :--- |
| **Parametric Design** | **Rhino 7 + Grasshopper** | Used for generating complex geometries and defining precise fabrication paths. |
| **Robotic Simulation** | **Robots Plugin (Vicente Soler)** | Essential for simulating UR3e kinematics and verifying coordinated motion planes. |
| **7th-Axis Computation** | **GHPython (Python 3)** | We developed custom scripts for Extended Inverse Kinematics (IK) to integrate the rotary gantry. |
| **Communication Middleware**| **Socket Messaging (TCP/IP)** | Our primary protocol for transmitting real-time motion commands from the workstation to the UR controller. |
| **Hardware Control** | **Arduino IDE / Firefly** | Used to program the microcontroller that manages the stepper/servo motor driver for the external axis. |
| **Native Robot Language** | **URScript** | We generate low-level scripts to ensure the UR3e executes fluid and safe movements. |
| **I/O Synchronization** | **Digital Input/Output (DIO)** | Logic implemented to ensure the robot and gantry synchronize their positions before proceeding. |

## 2. Operational Workflow (Data Flow)

Our integration follows a bidirectional logic to maintain precision throughout the process:

1. **Path Generation:** Geometry is processed within our Grasshopper environment to extract target planes.
2. **Axis Decomposition:** Our custom Python scripts calculate the necessary rotation for the 7th axis, optimizing the robot's reach and preventing singularities.
3. **Execution:** Commands are sent via TCP/IP. The UR3e and the rotary gantry perform a coordinated "handshake" using Digital I/O signals to guarantee operational safety.

## 3. Implementation Requirements

* **Network Stability:** We require a high-speed Ethernet connection between the workstation and the UR3e controller to minimize command latency.
* **Version Control:** All scripts and definitions are maintained in this repository to ensure our collective design changes do not disrupt the robotic logic.
* **Integrated Safety:** Our software stack leverages the native collaborative safety features of the UR3e, including force detection and emergency stop synchronization across the entire system.
