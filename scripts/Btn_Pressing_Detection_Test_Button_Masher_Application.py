#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 08:51:44 2021

@author: ret
"""

# @file Btn_Pressing_Detection_Test_Button_Masher_Application.py
#
# @brief Defines the test of the Button Pressing Detection using the Button Masher Application program.
#
# @section Btn_Pressing_Detection_Test_Button_Masher_Application Description
# Defines the test of the Button Pressing Detection using the Button Masher Application program.
# Test the efficiency of the Button Pressing Detection
# Using the same program than the Button Masher Application

#
# @section libraries_Button_Masher_Application Libraries/Modules
# - geometry_msgs.msg
# - pilz_robot_programming
# - math
# - rospy

from geometry_msgs.msg import Point
from pilz_robot_programming import *
import math
import rospy

__REQUIRED_API_VERSION__ = "1"



__REQUIRED_API_VERSION__ = "1" # API version
__ROBOT_VELOCITY__ = 0.5 #velocity of the robot

#main program
def start_program():
#    pick_pose_1= Pose(position=Point(-0.1, -0.45, 0.175), orientation=Quaternion(1, 0, 0, 0))
#    pick_pose_2= Pose(position=Point(0.05, -0.45, 0.175), orientation=Quaternion(1, 0, 0, 0))
#    intermediate_place_pose = Pose(position=Point(0.25, -0.25, 0.389), orientation=Quaternion(1, 0, 0, 0))
    intermediate_place_pose_orientation = Pose(position=Point(0.195, -0.585, 0.289), orientation=Quaternion(1, 1, 1, 1))
    i=0
    while i < 30:
#        rospy.loginfo("Move to intermediate_place_pose position") # log
#        r.move(Ptp(goal=intermediate_place_pose, vel_scale = __ROBOT_VELOCITY__, relative=False))
        rospy.loginfo("Move to intermediate_place_pose_orientation position") # log
        r.move(Ptp(goal=intermediate_place_pose_orientation, vel_scale = __ROBOT_VELOCITY__, relative=False))
        pick_and_place()
#        rospy.loginfo("Move to pick position") # log
#        r.move(Ptp(goal=pick_pose_1, vel_scale = __ROBOT_VELOCITY__, relative=False))
##        r.move(Ptp(goal=pick_pose_2, vel_scale = __ROBOT_VELOCITY__, relative=False))
#        rospy.loginfo("Pick movement") # log
#        pick_and_place()
        i+=1
       


def pick_and_place():    
    r.move(Lin(goal=Pose(position=Point(0, 0, 0.03)), reference_frame="prbt_tcp", vel_scale=0.1))
    rospy.loginfo("Open/Close the gripper") # log
    rospy.sleep(0.2)    # pick or Place the PNOZ (close or open the gripper)
    r.move(Lin(goal=Pose(position=Point(0, 0, -0.03)), reference_frame="prbt_tcp", vel_scale=0.1))
    

    
    
if __name__ == "__main__":
    rospy.init_node('robot_program_node')
    #initialisation
    r = Robot(__REQUIRED_API_VERSION__)
    start_program()