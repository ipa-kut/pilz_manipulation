#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 11:07:50 2021

@author: ret
"""

import rospy
import control_msgs.msg
from control_msgs.msg import JointTrajectoryControllerState
import datetime
from influxdb import InfluxDBClient

 ## Example to use it   
class PilzInformer(InfluxDBClient):
    def __init__(self):
        self.diagnostics_sub = rospy.Subscriber('/prbt/manipulator_joint_trajectory_controller/state', JointTrajectoryControllerState, self.diagnostics_callback)
        #self.clock_sub = rospy.Subscriber('clock', Clock, self.clock_callback)
        #self.temperature = '''rospy.Subscriber('temperature', Temperature, self.temperature_callback)''' # find the topic for temperature
        self.time_info = ""
        self.actual_joint_state= ()
        self.encoded_state=()
        self.error_state=()
        self.cartesian_position_end_effector=""
        self.temperature=""
        self.voltage=""
        self.client = InfluxDBClient(host="localhost",port="8086")

    def diagnostics_callback(self, diagnostics):
        self.actual_joint_state= diagnostics.actual.positions
        self.encoded_state=diagnostics.desired.positions
        self.error_state=diagnostics.error.positions
        self.write_into_db(self.client)
        self.data = self.write_info_json_into_db(self.client)
#        self.print_all_info()

    
    def print_all_info(self):
        print self.actual_joint_state
        print self.encoded_state

    def write_into_db(self,client):
        client.create_database('Pilz_Information_Test') ## Always writing in the same DB for now
        print(client.get_list_database())   ## This will be useful to chose the name of the database for each test
        client.switch_database('Pilz_Information_Test')
        
        
    def write_info_json_into_db(self,client):
        json_body = [
            {
                "measurement": "Pilz_Informations",
                "tags": {
                    "requestName": "Joint_State_Informations",
                    "requestType": "GET"
                },
                "time":datetime.datetime.utcnow(),
                 "fields": {
                    "actual_joint_state": str(self.actual_joint_state),
                    "encoded_state": str(self.encoded_state),
                    "error_state": str(self.error_state)
                            }
            }
        ]
        client.write_points(json_body)
    
    def clock_callback(self, clock):
        print clock


if __name__ == '__main__':
    rospy.init_node("joint_trajectory_subscriber", anonymous=True)
    myInformer = PilzInformer()
    rospy.spin()