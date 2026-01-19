# Data Architecture Flowchart | Project ArmFlip

This diagram illustrates the logical path of information from the initial design parameters to the physical execution of the 7th-axis system.

### [ DATA ARCHITECTURE FLOW ]

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

1. **Inverse Kinematics (IK) Solving:** Our Python script evaluates target planes.
2. **Command Distribution:** Pose data is sent via TCP/IP.
3. **The Handshake Protocol:** The robot and gantry use Digital I/O signals.
4. **Safety & Monitoring:** The system utilizes force-sensing to pause movement.
