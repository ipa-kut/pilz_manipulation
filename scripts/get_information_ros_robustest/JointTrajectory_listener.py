#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 14:53:05 2020

@author: ret
"""

import rospy
import control_msgs.msg
from control_msgs.msg import JointTrajectoryControllerState
#from control_msgs.msg import JointTrajectoryPoint
''' Definition of the topic listener of tool_pose '''



def callback(msg):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", msg.error.positions)





if __name__ == "__main__":
    # node initialization
    rospy.init_node("joint_trajectory_subscriber")
    # definition of publisher/subscriber and services
    rospy.Subscriber('/prbt/manipulator_joint_trajectory_controller/state', JointTrajectoryControllerState, callback)

    # endless loop till shut down
    rospy.spin()