#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 16:55:04 2020

@author: ret
"""

import rospy
import geometry_msgs.msg
from geometry_msgs.msg import PoseStamped
''' Definition of the topic listener of tool_pose '''



def callback(msg,th_E):
#    rospy.loginfo(rospy.get_caller_id() + "I heard %s", msg.pose.position)
#    define a paralellepiped rectangle as a volume where I am touching the button
    x = msg.pose.position.x
    y = msg.pose.position.y
    z = msg.pose.position.z
    if (x < th_E.x1_sup and x >th_E.x1_inf ) and (y  < th_E.y1_sup and y > th_E.y1_inf) and (z < th_E.z1_sup and z >th_E.z1_inf):
        th_E.bool_position_Btn1 = True
#        if th_E.bool_position_Btn1 == th_E.bool_position_Btn1_sendMsg:
#            print("send the socket message that the arm is in the Btn1 area")
#            th_E.bool_position_Btn1_sendMsg = False
    if (x > th_E.x1_sup or x < th_E.x1_inf) or (z > th_E.z1_sup) or (y > th_E.y1_sup or y < th_E.y1_inf):
        th_E.bool_position_Btn1  = False
#        if th_E.bool_position_Btn1 == th_E.bool_position_Btn1_sendMsg:
#            print("send the socket message that the arm has LEFT THE BTN1 AREA")
#            th_E.bool_position_Btn1_sendMsg = True
    if (x < th_E.x2_sup and x >th_E.x2_inf ) and (y  < th_E.y2_sup and y >th_E.y2_inf) and (z < th_E.z2_sup and z >th_E.z2_inf):
        th_E.bool_position_Btn2 = True
#        if th_E.bool_position_Btn2 == th_E.bool_position_Btn2_sendMsg:
#            print("send the socket message that the arm is in the Btn2 area")
#            th_E.bool_position_Btn2_sendMsg = False
    if (x > th_E.x2_sup or x < th_E.x2_inf) or (z > th_E.z2_sup) or (y > th_E.y2_sup or y < th_E.y2_inf):
        th_E.bool_position_Btn2  = False
#        if th_E.bool_position_Btn2 == th_E.bool_position_Btn2_sendMsg:
#            print("send the socket message that the arm has LEFT THE BTN2 AREA")
#            th_E.bool_position_Btn2_sendMsg = True




def run(th_E):
    print("COCOCOCOCOC")
    # node initialization
    rospy.init_node("tool_pose_publisher_use")
    # definition of publisher/subscriber and services
    rospy.Subscriber('tool_pose', PoseStamped, callback,th_E)

    # endless loop till shut down
    rospy.spin()