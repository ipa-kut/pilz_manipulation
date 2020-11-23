#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 15:59:29 2020

@author: ret
"""

import rospy
import class_thread_Emission
import class_thread_Reception
import socket,sys
import tool_pose_listener_socket_message

## find a way to automise that



def run(host,port):
    #Establishment of the connection :
    connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        connexion.connect((host, port))
    except socket.error:
        print "Connection has failed."
        sys.exit()    
    print "Connection established with the servor."
    try:
        th_E = class_thread_Emission.Thread_BtnPosition(connexion,"Btn1","Btn2",x1,y1,z1,x2,y2,z2)
        th_R = class_thread_Reception.ThreadReception(connexion)
        th_E.start()
        th_R.start()
    except KeyboardInterrupt :
        th_E._Thread__stop()
        th_R._Thread__stop()
        print("done")
    tool_pose_listener_socket_message.run(th_E)
    

if __name__ == '__main__':
    try:
        '''global variable I want to use '''
        # These are the cartesian position of the Btn
        #For now I use the position where the end effector should go
        x1 = -0.1
        y1 = -0.5
        z1 = 0.2
        x2 = 0.1
        y2 = -0.5
        z2 = 0.2
        print("lancement")
        host = '10.0.1.12'
        port = 50000
        run(host,port) # Define in which way and where we want to log the data 
    except rospy.ROSInterruptException:
        pass