# How the Process Works: Gantry & Robot Integration

---

## 1. Initialization Phase
At the start, the **Gantry** and **Robot** systems initialize simultaneously to ensure hardware synchronization.

* **Reach Validation:** The system performs a geometric check to confirm the target is within the gantry's physical workspace. 
    * *Failure:* Generates an **"Out of Reach"** error.
* **Active Safety:** LIDAR scanners activate immediately. 
    * *Failure:* Any detection of abnormal presence triggers an **Emergency Stop**.

---

## 2. Positioning Phase
The robot maneuvers to the initial coordinates to prepare for the first pass.

* **Target Offset:** Moves to a starting radius of **150mm** from the target.
* **Redundant Safety Check:** A "Double Reach" verification ensures the actuator is within the operational limits of both the gantry structure and the robot arm's kinematics.

---

## 3. Painting Phase (Nested Loops)
The core execution is managed through two nested `while` loops to ensure full coverage:

### **Logic Structure**
> **Outer Loop:** While `current angle` ≤ 360° (Complete Rotation)  
> **Inner Loop:** While `target height` > 0 (Top to Bottom)

### **Execution Steps:**
1.  **Spray Activation:** Engaging the spray gun.
2.  **Dynamic Adjustment:** The arm extension adjusts in real-time to maintain a constant distance from the surface.
3.  **Rotation:** Executes movement up to 360°.
4.  **Verification:** Deactivates spray gun and confirms **"Safety Zone Clear"**.
5.  **Iteration:** Decrements the target height (vertical step) and repeats the sequence.

---

## 4. Completion
Once the conditions of the loops are met:
* **Idle State:** The gantry returns to its home/idle position.
* **Power Down:** Scanners are deactivated.
* **Safe Exit:** The process concludes via a controlled emergency stop to ensure all systems remain locked.

---

## Safety Features Summary
| Feature | Function |
| :--- | :--- |
| **Continuous Verification** | Ongoing safety zone monitoring throughout the loops. |
| **Active LIDAR** | Real-time obstacle and breach detection. |
| **Multi-point E-Stops** | Ability to kill the process at any phase of the algorithm. |
| **Reach Verification** | Pre-movement checks to prevent mechanical strain or collisions. |
