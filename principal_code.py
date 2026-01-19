"""
Project: ArmFlip (Workshop 2.1)
This script calculates the 7th-axis rotation based on target reach 
and transmits pose data to the UR3e controller via TCP/IP.
"""

import socket
import math
import time

# Network Configuration for UR3e
ROBOT_IP = "192.168.1.100"  # Set to actual controller IP
PORT = 30002                # Secondary port for URScript execution

def solve_7th_axis(target_plane, robot_reach=0.5):
    """
    Calculates the 7th-axis rotation if the target point exceeds the robot's reach.
    """
    distance = target_plane.Origin.Length
    rotation_angle = 0.0
    
    if distance > robot_reach:
        # Axis Decomposition: calculate angle to bring the robot closer to the target
        rotation_angle = math.atan2(target_plane.Origin.Y, target_plane.Origin.X)
    
    return rotation_angle

def send_coordinated_command(pose, axis_angle):
    """
    Transmits the coordinated pose and synchronization signal via TCP/IP.
    """
    try:
        # Create Socket connection
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect((ROBOT_IP, PORT))
        
        # URScript Generation: Move command + Handshake signal
        # set_digital_out(1, True) triggers the external gantry movement
        command = "def arm_flip_move():\n"
        command += "  movej(p[{},{},{},{},{},{}], a=1.2, v=0.25)\n".format(*pose)
        command += "  set_digital_out(1, True)\n" 
        command += "end\n"
        
        s.send(command.encode('utf-8'))
        s.close()
        return "Status: Command Transmitted"
    except Exception as e:
        return "Error: Connection Failed - " + str(e)

# --- Main Execution Loop ---
if execute_motion:
    # 1. Kinematic Solving
    target_rotation = solve_7th_axis(input_plane)
    
    # 2. Data Transmission
    status = send_coordinated_command(formatted_pose, target_rotation)
    print(status)