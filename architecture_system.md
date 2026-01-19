# Data Architecture Flowchart | Project ArmFlip

This diagram illustrates the logical path of information from the initial design parameters to the physical execution of the 7th-axis system.

### [ DATA ARCHITECTURE FLOW ]

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
