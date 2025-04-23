from pyniryo import *
import time
import math

# Connect to robot
robot = NiryoRobot("10.10.10.10")  # Replace with actual IP
# Set up the workspace name
workspace_name = "final_ws"

robot.calibrate_auto()
robot.update_tool()


robot.move_joints(0.097,-0.263,-0.889,0.193,1.114,-0.054)
color_mix_times = {
    "orange": [2, 1, 0],     # R=2s, G=1s, B=0s
    "purple": [2, 0, 2],     # R=2s, G=0s, B=2s
    "green":  [0, 2, 0],     # R=0s, G=2s, B=0s
    "yellow": [2, 2, 0],     # R=2s, G=2s, B=0s
    "pink":   [2, 0, 1],     # R=2s, G=0s, B=1s
    "cyan":   [0, 2, 2],     # R=0s, G=2s, B=2s
    "white":  [1, 1, 1],     # R=1s, G=1s, B=1s
}
print(color_mix_times)
t1,t2,t3=color_mix_times[input("Please Enter the color you want to make - ")]
print(t1,t2,t3)
#observation point

if(t1):
    robot.open_gripper(400)
    robot.move_joints(0.097,-0.263,-0.889,0.193,1.114,-0.054)
    time.sleep(1)
    robot.move_joints(0.199,-0.341,-0.934,0.107,1.305,0.023)
    #2nd observation point
    robot.move_joints(0.191,-0.869,-0.782,0.072,1.62,0.019)
    robot.close_gripper(400)
    robot.move_joints(0.199,-0.341,-0.934,0.107,1.305,0.023)
    robot.move_joints(0.097,-0.263,-0.889,0.193,1.114,-0.054)
    robot.move_joints(-0.04,-0.263,-0.33,-0.038,0.446,0.029)
    time.sleep(1)
    robot.move_joints(-0.043,-0.285,-0.328,-0.009,-0.861,-0.166)
    time.sleep(1*t1)
    robot.move_joints(-0.04,-0.263,-0.33,-0.038,0.446,0.029)
    robot.move_joints(0.097,-0.263,-0.889,0.193,1.114,-0.054)
    time.sleep(1)
    robot.move_joints(0.199,-0.341,-0.934,0.107,1.305,0.023)
    robot.move_joints(0.191,-0.869,-0.782,0.072,1.62,0.019)
    robot.open_gripper(400)
    robot.move_joints(0.199,-0.341,-0.934,0.107,1.305,0.023)
    robot.move_joints(0.097,-0.263,-0.889,0.193,1.114,-0.054)
    

if(t2):
    robot.open_gripper(400)
    robot.move_joints(0.097,-0.263,-0.889,0.193,1.114,-0.054)
    robot.move_joints(-0.395,-0.302,-0.861,-0.497,1.095,0.184)
    time.sleep(1)

    #2nd observation point
    robot.move_joints(-0.404,-0.819,-0.773,-0.497,1.491,-0.023)
    robot.close_gripper(400)
    robot.move_joints(-0.395,-0.302,-0.861,-0.497,1.095,0.184)
    robot.move_joints(0.097,-0.263,-0.889,0.193,1.114,-0.054)
    # # Detect a cup-shaped object
    robot.move_joints(-0.04,-0.263,-0.33,-0.038,0.446,0.029)
    time.sleep(1)
    robot.move_joints(-0.043,-0.285,-0.328,-0.009,-0.861,-0.166)
    time.sleep(1*t2)
    robot.move_joints(-0.04,-0.263,-0.33,-0.038,0.446,0.029)
    robot.move_joints(0.097,-0.263,-0.889,0.193,1.114,-0.054)
    robot.move_joints(-0.395,-0.302,-0.861,-0.497,1.095,0.184)
    time.sleep(1)
    robot.move_joints(-0.404,-0.819,-0.773,-0.497,1.491,-0.023)
    robot.open_gripper(400)
    robot.move_joints(-0.395,-0.302,-0.861,-0.497,1.095,0.184)
    robot.move_joints(0.097,-0.263,-0.889,0.193,1.114,-0.054)



if(t3):
    robot.open_gripper(400)
    robot.move_joints(0.097,-0.263,-0.889,0.193,1.114,-0.054)
    time.sleep(1)
    robot.move_joints(0.909,-0.587,-0.443,0.888,1.356,-0.373)
    #2nd observation point
    robot.move_joints(0.865,-0.935,-0.361,0.815,1.357,-0.219)
    robot.close_gripper(400)
    robot.move_joints(0.909,-0.587,-0.443,0.888,1.356,-0.373)
    #robot.move_joints(0.097,-0.263,-0.889,0.193,1.114,-0.054)
    robot.move_joints(-0.04,-0.263,-0.33,-0.038,0.446,0.029)
    time.sleep(1)
    robot.move_joints(-0.043,-0.285,-0.328,-0.009,-0.861,-0.166)
    time.sleep(1*t3)
    robot.move_joints(-0.04,-0.263,-0.33,-0.038,0.446,0.029)
    #robot.move_joints(0.097,-0.263,-0.889,0.193,1.114,-0.054)
    time.sleep(1)
    robot.move_joints(0.909,-0.587,-0.443,0.888,1.356,-0.373)
    robot.move_joints(0.865,-0.935,-0.361,0.815,1.357,-0.219)
    robot.open_gripper(400)
    robot.move_joints(0.909,-0.587,-0.443,0.888,1.356,-0.373)
    robot.move_joints(0.097,-0.263,-0.889,0.193,1.114,-0.054)
    
    robot.move_joints(0.097,-0.263,-0.889,0.193,1.114,-0.054)
    
robot.close_connection()