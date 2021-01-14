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
import time_relativ_use
import write_influxdb
import write_csv



''' Define the Class BtnPosition to work faster'''
class Thread_BtnPosition(threading.Thread):    
    """! The Thread_BtnPosition class inherited from threading.Thread.
    Defines the ROS driver to define the button area.
    """    
    
    def __init__(self,conn,name_Btn1,name_Btn2,x1,y1,z1,x2,y2,z2,client_db,name_file):
        threading.Thread.__init__(self)
        """! The Thread_BtnPosition base class initializer as a thread .
        @param name  The name of the sensor.
        @return  An instance of the Sensor class initialized with the specified name.
        """        
        self.connection = conn
        self.name_Btn1 = name_Btn1
        self.name_Btn2 = name_Btn2
        ## Setting the area we want to detect the Robot is around the Btn
        self.x1_inf= x1-0.08
        self.x1_sup= x1+0.08 ## for now this is too much I guess
        self.y1_inf= y1-0.08 ## I do not know why I have a deviation in the trajectoy for the y coordonate
        self.y1_sup= y1+0.08
        self.z1_inf= z1-0.05
        self.z1_sup= z1+0.05
        self.x2_inf= x2-0.08
        self.x2_sup= x2+0.08
        self.y2_inf= y2-0.08 ## I do not know why I have a deviation in the trajectoy for the y coordonate
        self.y2_sup= y2+0.08
        self.z2_inf= z2-0.05
        self.z2_sup= z2+0.05
        self.bool_position_Btn1 = False
        self.bool_position_Btn1_sendMsg = True
        self.bool_position_Btn2 = False
        self.bool_position_Btn2_sendMsg = True
        self.msg_touched = "touched"
        self.msg_untouched = "untouched"
        self.client_db = client_db
        self.name_file = name_file

        

    def run(self):
        """! Retrieves the sensor's description.
        @return  send the socket message when the robot end effector enters or leave a button area.
        """
        while 1:
            if self.bool_position_Btn1 == self.bool_position_Btn1_sendMsg == True:
                time_relativ_use.time_t1 = datetime.datetime.utcnow() # defining the relativ time t1
                self.connection.send(str(datetime.datetime.utcnow())+";"+self.name_Btn1+";"+self.msg_touched)
                print("send the socket message that the arm is in the" + self.name_Btn1 +" area")               # to see on the screen the BtnPressing between the entering and going out of the BtnArea
                self.bool_position_Btn1_sendMsg = False                                                         # send the msg only once
            if self.bool_position_Btn1 == self.bool_position_Btn1_sendMsg == False:
                time_relativ_use.time_t2 = datetime.datetime.utcnow()
                self.connection.send(str(datetime.datetime.utcnow())+";"+self.name_Btn1+";"+self.msg_untouched)
                print("send the socket message that the arm has LEFT THE "+ self.name_Btn1 + "AREA")
                self.bool_position_Btn1_sendMsg = True
                if time_relativ_use.compare_time() == True:                                                     ## if the Btn is pressed during the interval of time we are in the area of the Btn
                    json_all_info = write_influxdb.json_body_define_allInfo(write_influxdb.list_msg)
                    self.client_db.write_points(json_all_info)
                    write_csv.write_into_csv(self.name_file,write_influxdb.list_msg)
                    print("writing is done")
                else: ## there is an error and we log this information as an error in the database
                    try:
                        print (write_influxdb.list_error)
                        json_error_info = write_influxdb.json_body_define_errorInfo(write_influxdb.list_error) ## we can defining there the type of error we want to deal with / add different type
                        self.client_db.write_points(json_error_info)
                    except:
                        pass
            ## same thing is done for the Btn2
            # I can change this into two threads each one dealing with one button / because good processing power on the computer (that was an issue on the Rpi, but should not be here)
            if self.bool_position_Btn2 == self.bool_position_Btn2_sendMsg == True:
                time_relativ_use.time_t1 = datetime.datetime.utcnow()
                self.connection.send(str(datetime.datetime.utcnow())+";"+self.name_Btn2+";"+self.msg_touched)
                print("send the socket message that the arm is in the" + self.name_Btn2 +" area")
                self.bool_position_Btn2_sendMsg = False
            if self.bool_position_Btn2 == self.bool_position_Btn2_sendMsg == False:
                time_relativ_use.time_t2 = datetime.datetime.utcnow()
                self.connection.send(str(datetime.datetime.utcnow())+";"+self.name_Btn2+";"+self.msg_untouched)
                print("send the socket message that the arm has LEFT THE "+ self.name_Btn2 + "AREA")
                self.bool_position_Btn2_sendMsg = True
                if time_relativ_use.compare_time() == True:              
                    json_all_info = write_influxdb.json_body_define_allInfo(write_influxdb.list_msg)
                    self.client_db.write_points(json_all_info)
                    write_csv.write_into_csv(self.name_file,write_influxdb.list_msg)
                else: 
                    try:
                        print (write_influxdb.list_error)
                        json_error_info = write_influxdb.json_body_define_errorInfo(write_influxdb.list_error)
                        self.client_db.write_points(json_error_info)
                    except:
                        pass
    

        
