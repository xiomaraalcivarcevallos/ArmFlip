# MRAC01(25/26): Workshop 2.1 - AIRFLIP - Rotary Gantry System for Small-Scale Cobots
## Index
  - [Overview](#overview) 
  - [Getting Started](#getting-started)
  - [Demo](#demo)
  - [Authors](#authors)
  - [References](#references)
  - [Credits](#credits)
<!--  Other options to write Readme
  - [Deployment](#deployment)
  - [Used or Referenced Projects](Used-or-Referenced-Projects)
-->
<!--Write a few sentences of academic context and project description -->  

## Overview

The initial idea and proposal for this project was to develop or propose an approach to how we can generate a flip somersault-like movement with a robotic arm, for which we researched on the internet about external axes or gantry systems. A gantry robot is a type of industrial robot, an automated piece of machinery applied in manufacturing or production, that utilizes a robot arm that is mounted either overhead on a rail system or a frame. In the gantry system, the beams hold up the robotic arm, creating an inflexible, stable structure. This arrangement allows gantry robots to move along the three linear axes: X, Y, and Z. They refer respectively to, horizontal movement from left to right, horizontal movement from the front to the back, and vertical movement up and down.

<img width="1177" height="632" alt="image" src="https://github.com/user-attachments/assets/06ffdbe4-ecd0-4d7f-89ad-86aba3417504" />

After analyzing these ideas, we decided to make some sketches about what would be most appropriate to implement for a cobot. First, we came up with a system that implements a rotating wheel system, which through guide rails allows the robot to move through that space. The second idea was to implement a structural system that elevates the robot, which also has a central rotary axis that allows it to perform the flip. We were able to visualize these sketches thanks to AI tools that allowed us to develop these images.

<img width="720" height="342" alt="Screenshot 2026-01-16 155040" src="https://github.com/user-attachments/assets/9c1b1d2a-1434-44e6-98b4-17721c375bb6" />
<img width="815" height="497" alt="image" src="https://github.com/user-attachments/assets/e512b953-55c7-4526-94c6-ee531e933830" />

After analyzing these ideas, we determined that the best approach to achieve this movement would be by implementing a Cartesian gantry system, since the previous ideas are less viable and more complex to develop. This project presents a 7th-Axis Rotary Gantry (External Axis) engineered to transcend the workspace limitations and kinematic constraints of compact collaborative robots. While cobots like the Universal Robots UR3e offer industry-leading precision, their 500 mm reach and fixed base often lead to kinematic singularities—mathematical points where the robot loses a degree of freedom and cannot move in specific directions—disqualifying them from large-format or complex industrial tasks.

**Core Innovation:** Our solution integrates the UR3e onto a rotary Robotic Transfer Unit (RTU). By introducing Kinematic Redundancy, we decouple the robot's motion from a static base. This "Workspace Multiplier" allows the system to bypass singularity zones (such as wrist alignment or elbow lock) by dynamically rotating the base. This ensures the robot can access areas and zones that are normally inaccessible due to the robot's inherent singularities, maintaining continuous, fluid motion throughout the entire process.

**Application Focus:** This proposal is specifically designed for artistic applications such as wall painting. The implementation of the gantry system would enable significant reductions in time and labor costs. With the gantry, the robot can reach numerous zones at angles that would be impossible to achieve without it. Additionally, it allows the robot to move with ease—moving up, down, rotating, and positioning itself according to specific needs—providing unprecedented flexibility for large-scale artistic work.

<img width="547" height="585" alt="image" src="https://github.com/user-attachments/assets/786f8d4c-7cf9-4eda-9a36-de3700555250" />

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

### Installing

1.  **Mechanical Integration:** Mount the UR3e onto the rotary platform. Ensure the center of mass is aligned with the gantry’s axis of rotation to minimize inertial load on the servo drive.
2.  **Driver Configuration:** Configure the industrial servo-drive to operate as a slave to the UR3e controller via the Fieldbus interface.
3.  **Kinematic Calibration & Singularity Mitigation:** Perform a Tool Center Point (TCP) and External Axis Calibration. The system is programmed to use the 7th axis as a **"Redundancy Resolver"**—if the arm's trajectory approaches a singularity, the gantry rotates to reposition the robot’s base, keeping the arm within its optimal dexterity range and reaching zones otherwise blocked by joint limits.

## Demo
The system operates using a **Coordinated Spiral Kinematic Path**:

![hello](https://github.com/user-attachments/assets/111619fb-c05f-4665-b8ae-f34c8c4df6e5)

* **Initialization:** The robot returns to "Home" position and initializes LiDAR-based area scanners for safety monitoring.
* **Surface Parameters:** The operator inputs the target structure's radius and vertical coverage height.
* **Execution:**
    * **The 7th Axis** provides a constant tangential velocity, effectively rotating the workspace to prevent the robot from reaching its mechanical limits.
    * **Singularity Avoidance:** By moving the base, the system ensures the UR3e never hits a "dead zone," allowing it to **reach areas or zones that the robot normally cannot reach** due to kinematic singularities.
    * **The UR3e Arm** dynamically adjusts its extension to maintain the optimal standoff distance (150 mm).
    * **The HVLP spray nozzle** is triggered, creating a seamless, uniform coating without the stuttering or stops caused by 6-axis kinematic locking.
* **Completion:** Upon reaching the target height, the system executes a cleaning cycle and generates a material consumption report.

## Authors
* **Xiomara Alcivar** – Mechatronics Engineer (System Design & Robotic Control).
* **Subha Tasin Saba** – Architect (Structural Design & Surface Optimization).
* **Yungsuan Lin** – Architect (Spatial Integration & Construction Planning).

## References
* [Universal Robots: UR3e Technical Specifications & Reach Study](https://www.universal-robots.com/products/ur3-robot/)
* [Mitsubishi Electric Automation: MELSERVO-J4 High-Performance Servo Systems](https://us.mitsubishielectric.com/fa/en/products/drive-products/ac-servos-melservo/melservo-j4)
* [NIST: Safety Standards for Collaborative Robotics](https://www.nist.gov/topics/robotics/collaborative-robots)
* [IEEE Xplore: Kinematic Control of 7-DOF Redundant Manipulators](https://ieeexplore.ieee.org/document/405903)

## Credits
* **Universal Robots A/S:** For providing the collaborative platform and the URCaps development ecosystem.
* **Mitsubishi Electric:** For the industrial-grade servo technology utilized in the rotary gantry.
* **Open Source Robotics Foundation (OSRF):** For simulation tools used to validate spiral trajectory planning.
* **Gemini AI:** For providing architectural logic support, technical protocol drafting, and optimization of kinematic redundancy strategies.
<!--  DO NOT REMOVE
-->
#### Acknowledgements

- Creation of GitHub template: [Marita Georganta](https://www.linkedin.com/in/marita-georganta/) - Robotic Sensing Expert
- Creation of MRAC-IAAC GitHub Structure: [Huanyu Li](https://www.linkedin.com/in/huanyu-li-457590268/) - Robotic Researcher


