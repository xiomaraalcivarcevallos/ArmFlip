# AIRFLIP - Rotary Gantry System for Small-Scale Cobots (UR3e)

## Overview
This project presents a **7th-Axis Rotary Gantry** (External Axis) engineered to transcend the workspace limitations of compact collaborative robots. While cobots like the **Universal Robots UR3e** offer industry-leading precision and safety, their **500 mm reach** often disqualifies them from large-format industrial tasks.

Our solution integrates the UR3e onto a rotary **Robotic Transfer Unit (RTU)**, transforming a desktop-class tool into a high-coverage industrial system. 

* **Target Application:** Automated precision coating and finishing for large cylindrical structures, tunnels, and architectural envelopes.
* **Core Innovation:** Decoupling the robot's kinematics from a fixed base to provide a "Workspace Multiplier" effect while maintaining the inherent safety protocols of collaborative robotics.

---

## Getting Started

### Prerequisites

#### Hardware
* **Robot:** Universal Robots **UR3e** (e-Series, Polyscope 5.x+).
* **Actuator:** Industrial AC Servo Motor (**Mitsubishi MELSERVO-J4** or **Panasonic Minas A6** Series) with IP65/67 rating to withstand paint particulates and overspray.
* **Transmission:** High-precision, low-backlash **Planetary Gearbox** (100:1 ratio).
* **Media Interface:** Industrial **Slip Ring** rated for Gigabit Ethernet (Profinet/EtherNet/IP) and high-pressure pneumatic supply.

#### Software
* **URCap** for External Axis integration and kinematic synchronization.
* **Communication Protocol:** EtherNet/IP or Modbus TCP for real-time motion handshaking.

### Installation & Setup
1.  **Mechanical Integration:** Mount the UR3e onto the rotary platform. Ensure the center of mass is aligned with the gantry’s axis of rotation to minimize inertial load on the servo drive.
2.  **Driver Configuration:** Configure the industrial servo-drive to operate as a slave to the UR3e controller via the Fieldbus interface.
3.  **Kinematic Calibration:** Perform a **Tool Center Point (TCP)** and **External Axis Calibration** to ensure the robot compensates for the gantry's angular displacement in its trajectory planning.

---

## Demo
The system operates using a **Coordinated Spiral Kinematic Path**:

1.  **Initialization:** The robot returns to "Home" position and initializes LiDAR-based area scanners for safety monitoring.
2.  **Surface Parameters:** The operator inputs the target structure's radius and vertical coverage height.
3.  **Execution:**
    * The **7th Axis** provides a constant tangential velocity for smooth rotation.
    * The **UR3e Arm** dynamically adjusts its extension to maintain the optimal standoff distance (150 mm).
    * The HVLP spray nozzle is triggered, creating a seamless, uniform coating without visible overlaps.
4.  **Completion:** Upon reaching the target height, the system executes a cleaning cycle and generates a material consumption report.

---

## Authors
* **Xiomara Alcivar** – *Mechatronics Engineer (System Design & Robotic Control).*
* **Subha Tasin Saba** – *Architect (Structural Design & Surface Optimization).*
* **Yungsuan Lin** – *Architect (Spatial Integration & Construction Planning).*

---

## References
* [Universal Robots: UR3e Technical Specifications & Reach Study](https://www.universal-robots.com/products/ur3-robot/)
* [Mitsubishi Electric Automation: MELSERVO-J4 High-Performance Servo Systems](https://www.mitsubishielectric.com/fa/products/drv/servo/index.html)
* [NIST: Safety Standards for Collaborative Robotics](https://www.nist.gov/el/intelligent-systems-division-73500/robotic-systems-smart-manufacturing)
* [IEEE Xplore: Kinematic Control of 7-DOF Redundant Manipulators](https://ieeexplore.ieee.org/document/108924)

---

## Credits
* **Universal Robots A/S:** For providing the collaborative platform and the URCaps development ecosystem.
* **Mitsubishi Electric:** For the industrial-grade servo technology utilized in the rotary gantry.
* **Open Source Robotics Foundation (OSRF):** For simulation tools used to validate spiral trajectory planning.
* **Gemini AI:** For providing architectural logic support and technical protocol drafting.
