#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Th Jan 28 11:55:10 2021

@author: alban, kut
"""
# @mainpage Doxygen Native Button Masher Application
# @file Button_Masher_Application.py
#
# @section Button_Masher_Application Description
# Press Button1 and send a socket message saying it is pressed
# Press Button2 and send a socket message saying it is pressed
# Repeat

from geometry_msgs.msg import Point
from pilz_robot_programming import *
import math
import rospy
import socket, sys
import time

__REQUIRED_API_VERSION__ = "1" # API version
__ROBOT_VELOCITY__ = 0.5 # Velocity of the robot
__SOCKET_HOST__ = '169.254.60.100'
__SOCKET_PORT__ = 65432

#main program
def start_program(loops, robot, connection):
    """! The Button Masher Application base function.
    @parameter loops is the number of sequence the robot is doing before stopping
    @parameter robot is the pilz robot API object
    @parameter connection is the socket connection
    Defines the sequence of the RET by going two ready position for each button, press it, and log the event
    """
    button1_pose= Pose(position=Point(-0.1, -0.45, 0.175), orientation=Quaternion(1, 0, 0, 0))
    button2_pose = Pose(position=Point(0.05, -0.45, 0.175), orientation=Quaternion(1, 0, 0, 0))
    i = 0
    while i <= loops:
        robot.move(Ptp(goal=button1_pose, vel_scale = __ROBOT_VELOCITY__, relative=False))
        rospy.sleep(0.2)
        press_and_log("button1", robot, connection)

        robot.move(Ptp(goal=button2_pose, vel_scale = __ROBOT_VELOCITY__, relative=False))
        rospy.sleep(0.2)
        press_and_log("button2", robot, connection)

        i+=1
        rospy.loginfo("We finished sequence number : %s" %i)
    connection.close()

def press_and_log(button_name, robot, connection):
    """! The press_and_log function.
    Go down to press the button, send a socket message logging the action, and go back up
    @param Name of button that was pressed
    """
    robot.move(Lin(goal=Pose(position=Point(0, 0, 0.03)), reference_frame="prbt_tcp", vel_scale=0.1))
    rospy.sleep(0.2)
    connection.send("prbt;" + str(time.time()) + ";" + button_name)
    robot.move(Lin(goal=Pose(position=Point(0, 0, -0.03)), reference_frame="prbt_tcp", vel_scale=0.1))
    rospy.sleep(0.2)

if __name__ == "__main__":
    rospy.init_node('robot_program_node')
    #initialisation
    r = Robot(__REQUIRED_API_VERSION__)
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        connection.connect((__SOCKET_HOST__, __SOCKET_PORT__))
    except socket.error:
        print("Connection has failed.")
        connection.close()
        sys.exit()
    print("Connection established with the servor.")
    start_program(loops=15000,robot=r, connection=connection )
