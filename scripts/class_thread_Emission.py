#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 16:04:57 2020

@author: ret
"""
import socket, sys, threading
      
import rospy
import tf
import geometry_msgs.msg
from geometry_msgs.msg import PoseStamped
import datetime



''' Define the Class BtnPosition to work faster'''
class Thread_BtnPosition(threading.Thread):
    def __init__(self,conn,name_Btn1,name_Btn2,x1,y1,z1,x2,y2,z2):
        threading.Thread.__init__(self)
        self.connection = conn
        self.name_Btn1 = name_Btn1
        self.name_Btn2 = name_Btn2
        self.x1_inf= x1-0.01
        self.x1_sup= x1+0.01
        self.y1_inf= y1-0.1 ## I do not know why I have a deviation in the trajectoy for the y coordonate
        self.y1_sup= y1+0.1
        self.z1_inf= z1-0.01
        self.z1_sup= z1+0.01
        self.x2_inf= x2-0.01
        self.x2_sup= x2+0.01
        self.y2_inf= y2-0.1 ## I do not know why I have a deviation in the trajectoy for the y coordonate
        self.y2_sup= y2+0.1
        self.z2_inf= z2-0.01
        self.z2_sup= z2+0.01
        self.bool_position_Btn1 = False
        self.bool_position_Btn1_sendMsg = True
        self.bool_position_Btn2 = False
        self.bool_position_Btn2_sendMsg = True
        self.msg_touched = "touched"
        self.msg_untouched = "untouched"

        
#    def run(self):
#        while 1:
#            if self.msg_jointState_bool_send == True:
#                self.connection.send(self.msg_jointState_complete)
#                self.msg_jointState_bool_send = False

    def run(self):
        while 1:
            if self.bool_position_Btn1 == self.bool_position_Btn1_sendMsg == True:
                self.connection.send(str(datetime.datetime.utcnow())+";"+self.name_Btn1+";"+self.msg_touched)
                print("send the socket message that the arm is in the" + self.name_Btn1 +" area")
                self.bool_position_Btn1_sendMsg = False
            if self.bool_position_Btn1 == self.bool_position_Btn1_sendMsg == False:
                self.connection.send(str(datetime.datetime.utcnow())+";"+self.name_Btn1+";"+self.msg_untouched)
                print("send the socket message that the arm has LEFT THE "+ self.name_Btn1 + "AREA")
                self.bool_position_Btn1_sendMsg = True
            if self.bool_position_Btn2 == self.bool_position_Btn2_sendMsg == True:
                self.connection.send(str(datetime.datetime.utcnow())+";"+self.name_Btn2+";"+self.msg_touched)
                print("send the socket message that the arm is in the" + self.name_Btn2 +" area")
                self.bool_position_Btn2_sendMsg = False
            if self.bool_position_Btn2 == self.bool_position_Btn2_sendMsg == False:
                self.connection.send(str(datetime.datetime.utcnow())+";"+self.name_Btn2+";"+self.msg_untouched)
                print("send the socket message that the arm has LEFT THE "+ self.name_Btn2 + "AREA")
                self.bool_position_Btn2_sendMsg = True
    

        
