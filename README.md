# AIRFLIP - Rotary Gantry System for Small-Scale Cobots (UR3e)

## Overview
This project presents a **7th-Axis Rotary Gantry** (External Axis) engineered to transcend the workspace limitations and kinematic constraints of compact collaborative robots. While cobots like the **Universal Robots UR3e** offer industry-leading precision, their **500 mm reach** and fixed base often lead to **kinematic singularities**—mathematical points where the robot loses a degree of freedom and cannot move in specific directions—disqualifying them from large-format or complex industrial tasks.

**Core Innovation:** Our solution integrates the UR3e onto a rotary Robotic Transfer Unit (RTU). By introducing **Kinematic Redundancy**, we decouple the robot's motion from a static base. This "Workspace Multiplier" allows the system to **bypass singularity zones** (such as wrist alignment or elbow lock) by dynamically rotating the base. This ensures the robot can access areas and zones that are normally inaccessible due to the robot's inherent singularities, maintaining continuous, fluid motion throughout the entire process.

---

## Target Application
Automated precision coating and finishing for large cylindrical structures, tunnels, and architectural envelopes where mechanical "dead zones" would otherwise cause process failure.

---

## Getting Started

### Prerequisites

#### Hardware
* **Robot:** Universal Robots UR3e (e-Series, Polyscope 5.x+).
* **Actuator:** Industrial AC Servo Motor (Mitsubishi MELSERVO-J4 or Panasonic Minas A6 Series) with IP65/67 rating to withstand paint particulates and overspray.
* **Transmission:** High-precision, low-backlash Planetary Gearbox (100:1 ratio).
* **Media Interface:** Industrial Slip Ring rated for Gigabit Ethernet (Profinet/EtherNet/IP) and high-pressure pneumatic supply.

#### Software
* **URCap** for External Axis integration and kinematic synchronization.
* **Communication Protocol:** EtherNet/IP or Modbus TCP for real-time motion handshaking.

---

## Installation & Setup

1.  **Mechanical Integration:** Mount the UR3e onto the rotary platform. Ensure the center of mass is aligned with the gantry’s axis of rotation to minimize inertial load on the servo drive.
2.  **Driver Configuration:** Configure the industrial servo-drive to operate as a slave to the UR3e controller via the Fieldbus interface.
3.  **Kinematic Calibration & Singularity Mitigation:** Perform a Tool Center Point (TCP) and External Axis Calibration. The system is programmed to use the 7th axis as a **"Redundancy Resolver"**—if the arm's trajectory approaches a singularity, the gantry rotates to reposition the robot’s base, keeping the arm within its optimal dexterity range and reaching zones otherwise blocked by joint limits.

---

## Demo

The system operates using a **Coordinated Spiral Kinematic Path**:

* **Initialization:** The robot returns to "Home" position and initializes LiDAR-based area scanners for safety monitoring.
* **Surface Parameters:** The operator inputs the target structure's radius and vertical coverage height.
* **Execution:**
    * **The 7th Axis** provides a constant tangential velocity, effectively rotating the workspace to prevent the robot from reaching its mechanical limits.
    * **Singularity Avoidance:** By moving the base, the system ensures the UR3e never hits a "dead zone," allowing it to **reach areas or zones that the robot normally cannot reach** due to kinematic singularities.
    * **The UR3e Arm** dynamically adjusts its extension to maintain the optimal standoff distance (150 mm).
    * **The HVLP spray nozzle** is triggered, creating a seamless, uniform coating without the stuttering or stops caused by 6-axis kinematic locking.
* **Completion:** Upon reaching the target height, the system executes a cleaning cycle and generates a material consumption report.

---

## Authors
* **Xiomara Alcivar** – Mechatronics Engineer (System Design & Robotic Control).
* **Subha Tasin Saba** – Architect (Structural Design & Surface Optimization).
* **Yungsuan Lin** – Architect (Spatial Integration & Construction Planning).

---

## References
* [Universal Robots: UR3e Technical Specifications & Reach Study](https://www.universal-robots.com/products/ur3-robot/)
* [Mitsubishi Electric Automation: MELSERVO-J4 High-Performance Servo Systems](https://us.mitsubishielectric.com/fa/en/products/drive-products/ac-servos-melservo/melservo-j4)
* [NIST: Safety Standards for Collaborative Robotics](https://www.nist.gov/topics/robotics/collaborative-robots)
* [IEEE Xplore: Kinematic Control of 7-DOF Redundant Manipulators](https://ieeexplore.ieee.org/document/405903)

---

## Credits
* **Universal Robots A/S:** For providing the collaborative platform and the URCaps development ecosystem.
* **Mitsubishi Electric:** For the industrial-grade servo technology utilized in the rotary gantry.
* **Open Source Robotics Foundation (OSRF):** For simulation tools used to validate spiral trajectory planning.
* **Gemini AI:** For providing architectural logic support, technical protocol drafting, and optimization of kinematic redundancy strategies.

---

## Acknowledgements
* Creation of GitHub template: Marita Georganta – Robotic Sensing Expert

* Creation of MRAC-IAAC GitHub Structure: Huanyu Li – Robotic Researcher
