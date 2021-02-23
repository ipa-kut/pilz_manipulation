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
        self.actual_state= ()
        self.encoded_state=()
        self.error_state=()
        self.cartesian_position_end_effector=""
        self.temperature=""
        self.voltage=""
        self.client = InfluxDBClient(host="localhost",port="8086",username='ret', password='asdf', database='demo')
        ## Get the pilz information about the name of the joint


    def diagnostics_callback(self, diagnostics):
        self.actual_state= diagnostics.actual.positions
        self.encoded_state=diagnostics.desired.positions
        self.error_state=diagnostics.error.positions
        self.write_into_db(self.client)
        self.data = self.write_info_json_into_db(self.client)
#        self.print_all_info()

    
    def print_all_info(self):
        print self.actual_state
        print self.encoded_state
        print self.error_state
    def write_into_db(self,client):
        client.create_database('demo') ## Always writing in the same DB for now
#        print(client.get_list_database())   ## This will be useful to chose the name of the database for each test
        client.switch_database('demo')
        
        
    def write_info_json_into_db(self,client):
        
        json_body_actual = [
            {
                "measurement": "actual_state",
                "tags": {
                    "requestName": "actual_state",
                    "requestType": "GET"
                },
                "time":datetime.datetime.utcnow(),
                 "fields": {
                    "prbt_joint1": self.actual_state[0],
                    "prbt_joint2": self.actual_state[1],
                    "prbt_joint3": self.actual_state[2],
                    "prbt_joint4": self.actual_state[3],
                    "prbt_joint5": self.actual_state[4],
                    "prbt_joint6": self.actual_state[5]
                            }
            }
        ]

        json_body_encoded = [
            {
                "measurement": "encoded_state",
                "tags": {
                    "requestName": "encoded_state",
                    "requestType": "GET"
                },
                "time":datetime.datetime.utcnow(),
                 "fields": {
                    "prbt_joint1": self.encoded_state[0],
                    "prbt_joint2": self.encoded_state[1],
                    "prbt_joint3": self.encoded_state[2],
                    "prbt_joint4": self.encoded_state[3],
                    "prbt_joint5": self.encoded_state[4],
                    "prbt_joint6": self.encoded_state[5]
                            }
            }
        ]
    
        json_body_error = [
            {
                "measurement": "error_state",
                "tags": {
                    "requestName": "error_state",
                    "requestType": "GET"
                },
                "time":datetime.datetime.utcnow(),
                 "fields": {
                    "prbt_joint1": self.error_state [0],
                    "prbt_joint2": self.error_state [1],
                    "prbt_joint3": self.error_state [2],
                    "prbt_joint4": self.error_state [3],
                    "prbt_joint5": self.error_state [4],
                    "prbt_joint6": self.error_state [5]
                            }
            }
        ]
   
        client.write_points(json_body_actual)
        client.write_points(json_body_encoded)
        client.write_points(json_body_error)
    
    def clock_callback(self, clock):
        print clock


if __name__ == '__main__':
    rospy.init_node("joint_trajectory_subscriber", anonymous=True)
    myInformer = PilzInformer()
    rospy.spin()