#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Th Jan 28 11:55:10 2021

@author: alban
"""
from geometry_msgs.msg import Point
from pilz_robot_programming import *
import math
import rospy


__REQUIRED_API_VERSION__ = "1" # API version
__ROBOT_VELOCITY__ = 0.5 #velocity of the robot

#main program
def start_program():
    """ To get the postion or to use a cartesian goal to move   
    print(r.get_current_pose())
    This is the equivalent of using the tf_node : rosrun tf tf_echo /prbt_base_link /prbt_tcp
    cartesian_goal=Pose(position=Point(0.020, -0.462, 0.396), orientation=Quaternion(0.772, 0.000, 0.000, 0.635))
    # Get the joint states
    print(r.get_current_joint_states())
    """
    pick_pose= Pose(position=Point(-0.1, -0.45, 0.175), orientation=Quaternion(1, 0, 0, 0))
    place_pose = Pose(position=Point(0.05, -0.45, 0.175), orientation=Quaternion(1, 0, 0, 0))
#    intermediate_place_pose = Pose(position=Point(0.05, -0.45, 0.389), orientation=Quaternion(1, 0, 0, 0))
#    intermediate_place_pose_orientation = Pose(position=Point(0.05, -0.45, 0.389), orientation=Quaternion(1, 1, 1, 1))
    #place_pose = Pose(position=Point(0.05, -0.45, 0.189), orientation=Quaternion(1, 1, 1, 1)) ### orientation that I want to try also
    i=0
    while i < 10000:
        r.move(Ptp(goal=pick_pose, vel_scale = __ROBOT_VELOCITY__, relative=False))
        pick_and_place()
        
        r.move(Ptp(goal=place_pose, vel_scale = __ROBOT_VELOCITY__, relative=False))
        pick_and_place()
        i+=1
        rospy.loginfo("We finished sequence number : %s" %i)
    rospy.loginfo("the program is stopped after number of sequence : %s" %i)
#        rospy.loginfo("Move to intermediate_place_pose position") # log
#        r.move(Ptp(goal=intermediate_place_pose, vel_scale = __ROBOT_VELOCITY__, relative=False))
#        rospy.loginfo("Move to intermediate_place_pose_orientation position") # log
#        r.move(Ptp(goal=intermediate_place_pose_orientation, vel_scale = __ROBOT_VELOCITY__, relative=False))
#        pick_and_place()
    
    


def pick_and_place():    
    r.move(Lin(goal=Pose(position=Point(0, 0, 0.03)), reference_frame="prbt_tcp", vel_scale=0.1))
    rospy.sleep(0.2)    # pick or Place the PNOZ (close or open the gripper)
    r.move(Lin(goal=Pose(position=Point(0, 0, -0.03)), reference_frame="prbt_tcp", vel_scale=0.1))
    

    
    
if __name__ == "__main__":
    rospy.init_node('robot_program_node')
    #initialisation
    r = Robot(__REQUIRED_API_VERSION__)
    start_program()