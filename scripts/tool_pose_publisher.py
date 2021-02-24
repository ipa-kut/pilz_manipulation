#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 16:59:12 2021

@author: ret
"""

# @file tool_pose_publisher.py
#
#
# @section tool_pose_publisher Description
# Define the global variable that the RET is using on the computer:
# - the end effector cartesian coordinates published in a topic
# - the name of the node publisher

#
# @section libraries_tool_pose_publisher Libraries/Modules
# - rospy for the use of ROS with python
# - tf
# - geometry_msgs.msg


import rospy
import tf
import geometry_msgs.msg
from geometry_msgs.msg import PoseStamped


if __name__ == '__main__':
    rospy.init_node('prbt_tool_pose_publisher')
    listener = tf.TransformListener()
    pub_tool_pose = rospy.Publisher('/tool_pose', PoseStamped,queue_size=10)

    seq = 0
    rate = rospy.Rate(10.0)

    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform('/prbt_flange', '/prbt_base_link', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue

        current_pose = geometry_msgs.msg.PoseStamped()
        current_pose.pose.position.x = trans[0]
        current_pose.pose.position.y = trans[1]
        current_pose.pose.position.z = trans[2]
        current_pose.pose.orientation.x = rot[0]
        current_pose.pose.orientation.y = rot[1]
        current_pose.pose.orientation.z = rot[2]
        current_pose.pose.orientation.w = rot[3]
        current_pose.header.frame_id="/prbt_tcp"
        current_pose.header.stamp = rospy.Time.now()
        current_pose.header.seq = seq
        seq += 1

        pub_tool_pose.publish(current_pose)
        
        rate.sleep()