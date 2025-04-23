# Colour_mixing_robot

Introduction :
This project involves automating a colour-mixing task using the Niryo One robotic
arm. The robot interacts with colour-coded cups placed at predefined locations on
the workspace. Using only the pyniryo Python library and Niryo Studio, we
program the robot to pick up coloured cups based on user input, move them to a
mixing station for a specified time, and then return them to their original positions.
The aim is to simulate colour mixing based on RGB time ratios in a collision-free
environment using predefined joint movements


Tools & Technologies Used :
• Hardware : Niryo One robotic arm
• Software :
◦ Niryo Studio : For initial calibration, workspace setup, and movement
planning
◦ Python : Main programming language
◦ pyniryo : Python API used to connect to and control the Niryo One


Objective :
To create a system where :
• A user inputs a desired colour.
• The robot identifies the required RGB components and their mixing duration.
• The robot picks each relevant colour cup from a predefined location, moves it
to the mixing area, simulates mixing by waiting, and then returns the cup to
its original place.
• Movements are predefined for each colour to avoid collisions between the
robotic arm and other objects or itself.


Methodology :
4.1 Workspace Setup
Using Niryo Studio, we defined a workspace named final_ws. In this workspace :
• Each colour cup (Red, Green, Blue) is assigned a fixed position.
• The mixing area is centrally located and also predefined.
• The robotic arm is calibrated using the auto-calibration feature to ensure
accuracy in positioning.


4.2 Colour-Time Mapping
The mixing time for each RGB component is predefined and stored in a dictionary :
python :
color_mix_times = {
    "orange": [2, 1, 0],     # R=2s, G=1s, B=0s
    "purple": [2, 0, 2],     # R=2s, G=0s, B=2s
    "green":  [0, 2, 0],     # R=0s, G=2s, B=0s
    "yellow": [2, 2, 0],     # R=2s, G=2s, B=0s
    "pink":   [2, 0, 1],     # R=2s, G=0s, B=1s
    "cyan":   [0, 2, 2],     # R=0s, G=2s, B=2s
    "white":  [1, 1, 1],     # R=1s, G=1s, B=1s
}
Each value represents the amount of time (in seconds) the respective colour (Red,
Green, Blue) needs to be "mixed" for a particular final colour.

4.3 Program Flow (Python Script)
1. Connection and Calibration
The robot connects to the IP 10.10.10.10, calibrates itself, and updates its
tool (gripper).
2. User Input
The user is prompted to input a colour. The system extracts the respective
RGB mixing times from the dictionary.
3. Sequential Colour Handling
For each non-zero RGB value :
◦ The robot opens the gripper.
◦ Moves to the respective cup's location using predefined joint values.
◦ Closes the gripper to pick the cup.
◦ Returns to the mixing area.
◦ Waits for the specified duration to simulate mixing.
◦ Returns the cup to its original location.
4. Path Planning
All joint positions (robot.move_joints(...)) are predefined to ensure :
◦ Accurate pickups and placements.
◦ Collision-free movement paths for each colour cup.
◦ Smooth transitions between pickup, mixing, and drop-off locations.
5. Disconnection
After processing all components, the robot safely closes its connection.


Collision Avoidance :
Each colour has a dedicated sequence of joint positions for :
• Pickup
• Movement to the mixing zone
• Return to original position
These joint values were manually tested and fine-tuned using Niryo Studio to ensure
• No overlapping paths
• Safe operation with multiple objects present
• Smooth transitions between tasks


Conclusion :
This project demonstrates the successful use of the Niryo One robotic arm to
simulate colour mixing tasks through RGB component handling. By defining safe
and efficient movement paths, and utilising the pyniryo API and Niryo Studio, we
built a simple yet robust robotic workflow that simulates real-world automation
principles in a controlled environment.
