# ArmFlip - GROUP4
### Saba, Xio, Yunghsuan

### Main Goal
Develop an external tool that allows a Kinova Gen3 Lite robot arm to perform a complete flip, replicating natural human movement.

### Scope
- **Main System**: Kinova Gen3 Lite robot arm
- **System to Develop**: External tool/mechanism that enables flip motion
- **Target Movement**: Complete 360° flip

### Functional Requirements
 **Movement**
   - Complete controlled 360° rotation
   - Maintain stability during rotation
   - Return to starting position in controlled way

 **Control**
   - Integration with Kinova Kortex API (ROS 2, Python, C++)
   - Programmable and repeatable movement
   - Safety system (emergency stop)
   - Low-level control.

## CONCEPT EXPLORATION 

### CONCEPT 1: Rotating Base Platform 🔄
**Description**: Motorized circular platform that rotates 360° on central axis, carrying the Kinova Gen3 Lite through complete rotation.

#### Proposed Design:
```
Side View:
    [Kinova Gen3 Lite]
         |||
    ===============  ← Circular platform (diameter ~1.2-1.5m)
         |||
      [DC Motor]
         |||
    ___Fixed Base___
```
<img width="1024" height="1536" alt="image" src="https://github.com/user-attachments/assets/1bd21b31-0e07-494f-b2bb-ce6a8a641f25" />

#### Advantages:
✅ **Precise and smooth control**: Electronically controlled motor allows variable speed
✅ **Predictable movement**: Rotation on fixed axis, easy to program
✅ **High repeatability**: Same movement every time
✅ **Kortex API integration**: Synchronization between base motor and arm joints

#### Disadvantages:
⚠️ Motor needs sufficient torque 
⚠️ Requires quality bearings for smooth movement
⚠️ Minimum diameter ~1.2m for extended arm clearance
⚠️ Doesn't fully replicate "natural" flip movement

---

### CONCEPT 2: Circular Rail System (Track System) 🎡
**Description**: Wheel-like circular structure with rails/track where arm mounts and moves 360°, similar to a ferris wheel.

#### Proposed Design:
```
Front View:
       ╱‾‾‾‾‾‾‾‾╲
      ∣   [Kinova]  ∣  ← Mounted on moving cart
     ∣    ═══════    ∣  ← Circular rails
     ∣              ∣
      ∣            ∣
       ╲__________╱
           |||
       [Motor/Axis]
```
<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/5a5b13f4-70df-403f-8ef2-e1fa830feacb" />

#### Advantages:
✅ **More "natural" movement**: Simulates flip trajectory with translation
✅ **Visually spectacular**: Complete wheel effect
✅ **Scalable**: Can vary diameter as needed
✅ **Multiple possible configurations**: Vertical, horizontal, or inclined
✅ **Lower motor torque**: Forces distributed in structure

#### Disadvantages:
⚠️ More complex structure to build 
⚠️ Cart/trolley sliding system needed
⚠️ More complex data/power transfer 
⚠️ More space required (minimum diameter ~2m for safety)

---


### PHASE 2: System Design (Functional Baseline)
**Estimated Duration**: 3-4 weeks

**Activities:**
- Detailed 3D modeling of selected concept
- Basic finite element analysis (FEA)
- Define control architecture
- Kinematic simulation of movement
- Define interfaces with robot arm

**Deliverables:**
- Complete 3D CAD models
- System architecture diagrams
- Detailed technical specifications
- Preliminary bill of materials (BOM)
- Control plan and algorithms

**Milestone**: Technical Review - Preliminary Design

---

### PHASE 3: Detailed Design (Allocated Baseline)
**Estimated Duration**: 3-4 weeks

**Activities:**
- Detailed manufacturing drawings
- Control code development
- Complete system simulations
- Cost analysis and component sourcing
- Technical documentation

**Deliverables:**
- Manufacturing drawings with tolerances
- Source code v1.0
- Validated simulation of complete movement
- Detailed budget
- Preliminary technical manual

**Milestone**: Design Review - Approval for Manufacturing

---

### PHASE 4: Integration and Demonstration
**Estimated Duration**: 4-5 weeks

**Activities:**
- Component fabrication/acquisition
- Prototype assembly
- Integration with robot arm
- Incremental testing (no movement → low speed → full speed)
- Adjustments and optimization
- Final demonstration

**Deliverables:**
- Functional prototype
- Test and validation results
- Demonstration video
- Final project documentation
- Lessons learned

**Milestone**: System Demonstration - Project Complete

---

## 6. TEAM STRUCTURE (IPT - Integrated Product Team)

### Roles and Responsibilities

**Systems Lead / Technical Manager**
- Coordinate integration of disciplines
- Manage schedule and milestones
- Main point of contact

**Mechanical Designer / 3D**
- CAD 3D modeling
- Structural analysis
- Material selection
- Manufacturing drawings

**Sketch Designer / Conceptualization**
- Visual exploration of concepts
- Movement storyboarding
- Graphic documentation
- Presentations

**Programmer / Control**
- Control algorithm development
- Hardware integration
- Software simulations
- Code testing

**Robotics Specialist (if applicable)**
- Interface with existing robot arm
- Kinematics and dynamics
- Calibration

### Team Meetings
- **Daily standup** (15 min): progress and blockers
- **Weekly review** (1 hour): detailed technical review
- **Sprint planning** (at start of each phase)
- **Milestone reviews** (at end of each phase)
