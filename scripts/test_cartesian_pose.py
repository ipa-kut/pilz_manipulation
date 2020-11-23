#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 13:59:37 2020

@author: ret
"""

from geometry_msgs.msg import Pose, Point
from pilz_robot_programming import *
import math
import rospy

__REQUIRED_API_VERSION__ = "1" # API version
__ROBOT_VELOCITY__ = 0.5 #velocity of the robot

#main program
def start_program():
    """ To get the postion or to use a cartesian goal to move   
    print(r.get_current_pose())
    ## This is the equivalent of using the tf_node : rosrun tf tf_echo /prbt_base_link /prbt_tcp
    cartesian_goal=Pose(position=Point(0.020, -0.462, 0.396), orientation=Quaternion(0.772, 0.000, 0.000, 0.635))
    # Get the joint states
    print(r.get_current_joint_states())
    """
    
    # important positions
    start_pos = [1.49, -0.54, 1.09, 0.05, 0.91,-1.67]   # joint values
    pick_pose= Pose(position=Point(-0.1, -0.5, 0.4), orientation=Quaternion(1, 0, 0, 0.1))

    rospy.loginfo("Move to pick position") # log
    r.move(Ptp(goal=pick_pose, vel_scale = __ROBOT_VELOCITY__, relative=False))
    print(r.get_current_pose())
    r.move(Lin(goal=Pose(position=Point(0, 0, 0.1)), reference_frame="prbt_tcp", vel_scale=0.1))
    print(r.get_current_pose())
    

def pick_and_place():    
    r.move(Lin(goal=Pose(position=Point(0, 0, 0.1)), reference_frame="prbt_tcp", vel_scale=0.1))
    rospy.loginfo("Open/Close the gripper") # log
    rospy.sleep(0.2)    # pick or Place the PNOZ (close or open the gripper)
    r.move(Lin(goal=Pose(position=Point(0, 0, -0.1)), reference_frame="prbt_tcp", vel_scale=0.1))
    
    
if __name__ == "__main__":
    rospy.init_node('robot_program_node')
    #initialisation
    r = Robot(__REQUIRED_API_VERSION__)
    start_program()