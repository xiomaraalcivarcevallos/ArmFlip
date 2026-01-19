# Technical Documentation | Project ArmFlip

This document consolidates the software requirements, system architecture, and operational workflows developed by our team for the **ArmFlip** project (Workshop 2.1). Our goal is to synchronize a **UR3e collaborative robot** with a custom **7th-axis rotary gantry** to expand the reach and flexibility of the fabrication process.

---

## 1. Software Stack & System Requirements

We have established the following technical ecosystem to manage the coordination between parametric design and robotic execution:

| Layer | Tool | Team's Implementation |
| :--- | :--- | :--- |
| **Design** | **Rhino 7 + Grasshopper** | Generation of geometry and precise fabrication paths. |
| **Simulation** | **Robots Plugin** | Verification of UR3e kinematics and motion planes. |
| **Computation** | **GHPython (Python 3)** | Custom solvers for Extended Inverse Kinematics (IK) and 7th-axis decomposition. |
| **Middleware** | **TCP/IP Socket / Serial** | Real-time communication protocols for the robot and external motor driver. |
| **Firmware** | **URScript / Arduino** | Low-level logic for fluid hardware execution and motor control. |
| **Sync** | **Digital I/O (DIO)** | Logic ensuring hardware-level synchronization through a handshake protocol. |

---

## 2. Data Architecture Flow

This diagram illustrates the logical path of information from the initial design parameters to the physical execution.

```text
[ 1. DESIGN LAYER ]
       |
       v
+-----------------------------+      +---------------------------+
|  Rhino + Grasshopper Logic  | ---> |  Geometry & Path Targets  |
+-----------------------------+      +---------------------------+
                                             |
[ 2. COMPUTATIONAL LAYER ]                   |
                                             v
                             +-------------------------------+
                             |  GHPython Kinematic Solver    |
                             |  (Axis Decomposition Logic)   |
                             +-------------------------------+
                                     /               \
                [Stream A: Robot Data]               [Stream B: Gantry Data]
                          |                                    |
[ 3. MIDDLEWARE LAYER ]   v                                    v
                +--------------------+               +-----------------------+
                | TCP/IP Socket Msg  |               | Serial / USB Command  |
                +--------------------+               +-----------------------+
                          |                                    |
[ 4. HARDWARE LAYER ]     v                                    v
                +--------------------+               +-----------------------+
                |  UR3e Controller   | <-----------> | Arduino + Motor Driver|
                +--------------------+   (I/O Sync)  +-----------------------+
                          |                                    |
                          \________________  __________________/
                                           \/
                                  [ COORDINATED MOTION ]
```
## 3. Operational Workflow (Step-by-Step)

To ensure precision and safety during the fabrication of our prototypes, the system follows this sequence:

Inverse Kinematics (IK) Solving: Our Python script evaluates target planes. If a point is outside the UR3e’s reach, the script calculates the optimal rotation for the 7th axis.

Command Distribution: Pose data is sent to the UR3e via TCP/IP, while angular steps are sent to the gantry motor via Serial.

The Handshake Protocol: The robot and gantry use Digital I/O signals to confirm they have reached their targets before triggering the next movement.

Safety & Monitoring: The system utilizes the UR3e's native force-sensing to pause all data streams and hardware movement if resistance or a collision is detected.
