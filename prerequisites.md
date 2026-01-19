\# Prerequisites \& Technical Requirements | Project ArmFlip



To successfully implement the 7th-axis integration and run the control scripts, the following software, libraries, and tools must be installed and configured.



| Category | Item | Description |

| :--- | :--- | :--- |

| \*\*Design Engine\*\* | \*\*Rhino 7 / 8\*\* | Core environment for parametric modeling and geometry generation. |

| \*\*Visual Scripting\*\* | \*\*Grasshopper\*\* | Main interface for toolpath generation and robotic logic. |

| \*\*Python Libraries\*\* | \*\*`socket` \& `struct`\*\* | Native Python modules used for TCP/IP communication with the UR3e. |

| \*\*GH Plugins\*\* | \*\*Robots (Vicente Soler)\*\* | Required for UR3e kinematic visualization and plane transformation. |

| \*\*IDE\*\* | \*\*Arduino IDE 2.0+\*\* | Environment to compile and upload the 7th-axis firmware to the controller. |

| \*\*Arduino Library\*\* | \*\*AccelStepper\*\* | \*\*Essential:\*\* Must be installed via Library Manager to handle motor acceleration. |

| \*\*Middleware\*\* | \*\*TCP/IP \& Serial\*\* | Established communication protocols between the PC, Robot, and Arduino. |

| \*\*Hardware Ref.\*\* | \*\*URScript Manual\*\* | Technical reference for low-level robot commands (movej, set\_digital\_out). |

| \*\*Network\*\* | \*\*Ethernet Cat6\*\* | Required for a stable, low-latency connection between the PC and UR3e. |



\## Installation Steps for the Team



1\. \*\*Arduino Library:\*\* Open Arduino IDE -> Sketch -> Include Library -> Manage Libraries -> Search for \*\*"AccelStepper"\*\* and install the latest version.

2\. \*\*Grasshopper Setup:\*\* Ensure the \*\*Robots\*\* plugin is installed in your Components folder. This is vital for simulating our reach before physical testing.

3\. \*\*Network Configuration:\*\* Set a static IP on your workstation (e.g., `192.168.1.10`) to ensure the Python `socket` script can find the UR3e controller at its assigned address.

4\. \*\*Hardware Handshake:\*\* Refer to the UR3e controller manual to identify Digital Output 1 and Digital Input 1 for the physical synchronization wiring.

