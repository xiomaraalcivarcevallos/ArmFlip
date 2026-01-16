# Gantry Painting System: Operational Steps

---

## 1. System Initialization & Safety Check
* **Startup:** Power on the Gantry System and the UR3e Robot.
* **Hardware Sync:** The system initializes the **Slip Ring** and the **spray gun**.
* **Safety Protocol:** The **LIDAR Safety Scanners** must be activated immediately.

> [!IMPORTANT]
> **Emergency Stop:** If the LIDAR fails or the target is "Out of Reach," the system will trigger an automatic Emergency Stop.

---

## 2. Positioning
* The robot moves to the designated **Start Position**.
* **Radius:** Maintains a specific distance of **-150mm** from the target.
* **Reach Verification:** The system verifies that the target remains within the gantry’s physical reach before starting.

---

## 3. Painting Process (Execution)
*The system operates in a continuous loop until the **Target Height** reaches **0**:*

1.  **Spray Activation:** The spray gun activates while the arm adjusts its extension to maintain a constant distance.
2.  **Rotation:** The robot rotates around the object (up to 360°).
3.  **Vertical Step:** Once a rotation is complete, the robot decrements the height (moves down one level) and repeats the cycle.

---

## 4. Safety Monitoring
* **Constant Surveillance:** The **"Safety Zone Clear?"** check runs continuously.
* **Breach Protocol:** Any breach detected by the LIDAR or a system error will lead to an **Emergency Stop**, instantly killing the algorithm to prevent accidents.

---

## 5. Shut Down
* **Idle Mode:** Once the painting is finished, the Gantry enters Idle Mode.
* **Deactivation:** LIDAR scanners are deactivated.
* **Exit:** The process ends, and the algorithm exits safely.
