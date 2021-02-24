#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Th Jan 28 11:55:10 2021

@author: alban
"""
# @mainpage Doxygen Native Button Masher Application
# @file Button_Masher_Application.py
#
# @section Button_Masher_Application Description
# Define the global variable that the RET is using on the computer:
# - the required API version
# - the robot velocity
# - the name of the node

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


__REQUIRED_API_VERSION__ = "1" # API version
__ROBOT_VELOCITY__ = 0.5 #velocity of the robot

#main program
def start_program(i):
    """! The Button Masher Application base function.
    @parameter i is the number of sequence the robot is doing before stopping
    Defines the sequence of the RET by going two ready position and then have a sequence of linear movement.
    """
    pick_pose= Pose(position=Point(-0.1, -0.45, 0.175), orientation=Quaternion(1, 0, 0, 0))
    place_pose = Pose(position=Point(0.05, -0.45, 0.175), orientation=Quaternion(1, 0, 0, 0))
    #define a sequence instead of the pick and place application: With it, the robot remember that he already made the sequence
    blend_sequence = Sequence()
    blend_sequence.append(Lin(goal=Pose(position=Point(0, 0, 0.03)), reference_frame="prbt_tcp", vel_scale=0.1))
    blend_sequence.append(Lin(goal=Pose(position=Point(0, 0, -0.015)), reference_frame="prbt_tcp", vel_scale=0.1))
    while i < 15000:
        r.move(Ptp(goal=pick_pose, vel_scale = __ROBOT_VELOCITY__, relative=False))
        rospy.sleep(0.2)
        r.move(blend_sequence)
#        pick_and_place()
#
        r.move(Ptp(goal=place_pose, vel_scale = __ROBOT_VELOCITY__, relative=False))
        rospy.sleep(0.2)
        r.move(blend_sequence)
#        pick_and_place()

        i+=1
        rospy.loginfo("We finished sequence number : %s" %i)
            

#        rospy.loginfo("Move to intermediate_place_pose position") # log
#        r.move(Ptp(goal=intermediate_place_pose, vel_scale = __ROBOT_VELOCITY__, relative=False))
#        rospy.loginfo("Move to intermediate_place_pose_orientation position") # log
#        r.move(Ptp(goal=intermediate_place_pose_orientation, vel_scale = __ROBOT_VELOCITY__, relative=False))
#        pick_and_place()
    
    


def pick_and_place():    
    """! The Button Masher Application Pick and Place function.
    Changed by a sequence in the function for it to be reminded
    """
    r.move(Lin(goal=Pose(position=Point(0, 0, 0.03)), reference_frame="prbt_tcp", vel_scale=0.1))
    rospy.sleep(0.2)    # pick or Place the PNOZ (close or open the gripper)
    r.move(Lin(goal=Pose(position=Point(0, 0, -0.03)), reference_frame="prbt_tcp", vel_scale=0.1))
    rospy.sleep(0.2)    # pick or Place the PNOZ (close or open the gripper)

    
    
if __name__ == "__main__":
    rospy.init_node('robot_program_node')
    #initialisation
    r = Robot(__REQUIRED_API_VERSION__)
    start_program(i=0)
