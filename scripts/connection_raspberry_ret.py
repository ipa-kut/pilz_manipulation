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
import write_influxdb
import write_csv



def main(x1,y1,z1,x2,y2,z2,host,port):
    """! Main program entry."""
    """! Maps a number from one range to another.
    @param x1 @param y1 @param z1   The input number for the position of the target pose 1
    @param x2 @param y2 @param z2   The input number for the position of the target pose 2
    @param host @param port   The input number for the socket connection
    @nparam ame_file    The name of the csv file we are logging the information in
    @param client_db    The influx db we are using
    
    @return Set the socket communication and launch the commucation between the Button Masher Application and the Test
    """
    try:
        # I use the position of the end effector 
        ''' To use with the endurance_demo launch'''
        print("lancement")

            #Establishment of the connection :
        connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            connexion.connect((host, port))
        except socket.error:
            print "Connection has failed."
            sys.exit()    
        print "Connection established with the servor."

#        run(connexion,client_db,name_file) # Define in which way and where we want to log the data 
#            """! Main program entry."""
        try:
            #starting the thread
            th_E = class_thread_Emission.Thread_BtnPosition(connexion,"Btn1","Btn2",x1,y1,z1,x2,y2,z2,client_db,name_file)
            th_R = class_thread_Reception.ThreadReception(connexion)
            th_E.start()
            th_R.start()
        except KeyboardInterrupt :
            th_E._Thread__stop()
            th_R._Thread__stop()
            print("done") # in order to know that we have well shutdown the thread when we end the test
        tool_pose_listener_socket_message.run(th_E) ## this is the node hearing the tool_pose_position and telling the th_Emission to send the msg to the Rpi
    except rospy.ROSInterruptException or KeyboardInterrupt:
        connexion.close()
        print("Close the socket communication")
        pass
    
if __name__ == '__main__':
    x1 = -0.1
    y1 = -0.5
    z1 = 0.319 -0.03 # -0.03 is the argument we gave to the pick and place to deal with
    x2 = 0.05
    y2 = -0.5
    z2 = 0.319 -0.03 
    host = '10.4.11.117'
    port = 5003
    name_file = write_csv.create_csv_file(write_csv.header, write_csv.name_file)
    client_db = write_influxdb.write_into_db()
    main(x1,y1,z1,x2,y2,z2,host,port)
