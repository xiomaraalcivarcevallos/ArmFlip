"""
Project: ArmFlip (Workshop 2.1)
This script calculates the 7th-axis rotation based on target reach 
and transmits pose data to the UR3e controller via TCP/IP.
"""
import numpy as np
import rtde_control
import rtde_receive
import time

class AirFlipSystem:
    """
    Core controller for the AIRFLIP project.
    Synchronizes a UR3e cobot with a 7th-axis rotary gantry.
    """
    def __init__(self, robot_ip):
        try:
            self.rtde_c = rtde_control.RTDEControlInterface(robot_ip)
            self.rtde_r = rtde_receive.RTDEReceiveInterface(robot_ip)
            print(f"Connected to UR3e at {robot_ip}")
        except Exception as e:
            print(f"Connection failed: {e}")

    def compute_7th_axis_compensation(self, target_pose, gantry_theta):
        """
        Adjusts the target Cartesian pose based on the gantry's rotation.
        target_pose: [x, y, z, rx, ry, rz]
        gantry_theta: Rotation of the base in radians.
        """
        # Rotation matrix for the Z-axis (Gantry axis)
        R_z = np.array([
            [np.cos(gantry_theta), -np.sin(gantry_theta), 0],
            [np.sin(gantry_theta),  np.cos(gantry_theta), 0],
            [0,                    0,                    1]
        ])

        # Extract position and apply rotation
        pos_b = np.array(target_pose[:3])
        pos_compensated = R_z.dot(pos_b)

        # Reconstruct the pose with the same orientation
        return list(pos_compensated) + target_pose[3:]

    def execute_synchronized_flip(self, target_pose, gantry_angle):
        """
        Sends simultaneous commands to the gantry (via C++ bridge) and UR3e.
        """
        compensated_pose = self.compute_7th_axis_compensation(target_pose, gantry_angle)
        
        # In a real scenario, here we trigger the C++ hardware_controller
        print(f"Syncing: Gantry at {np.degrees(gantry_angle)}° | Robot moving to {compensated_pose[:3]}")
        
        # Execute movement on the robot
        self.rtde_c.moveL(compensated_pose, 0.2, 0.3)

if __name__ == "__main__":
    # Example usage for the team
    AIRFLIP = AirFlipSystem("192.168.1.10")
    
    # Target: Stay at [0.3, 0.2, 0.4] relative to ground while base rotates 90 deg
    target = [0.3, 0.2, 0.4, 0, 3.14, 0]
    AIRFLIP.execute_synchronized_flip(target, np.deg2rad(90))
