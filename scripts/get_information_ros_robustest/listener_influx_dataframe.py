#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 12:10:12 2021

@author: ret
"""

import argparse
import pandas as pd
from influxdb import DataFrameClient


class influx_logging():
    def __init__(self,host,port,user,password,dbname):
        self.host = host
        self.port = port
        self.user = 'ret'
        self.password = 'asdf'
        self.dbname = 'demo'
        self.protocol = 'line'
        self.client = DataFrameClient(self.host, self.port, self.user, self.password, self.dbname)
        pass
    
    def main(self,actual_joint_state,encoded_joint_state):
        print("Create database: " + self.dbname)
        self.client.create_database(self.dbname)
        
        print("Write DataFrame with Tags")
        df = pd.DataFrame(data=list(range(1)),
              index=pd.date_range(start=datetime.datetime.utcnow(),
                                  periods=1, freq='H'),columns=['num_data_df'])
        self.client.write_points(df, 'actual_joint_state',
                                 {'joint1': actual_joint_state[0], 'joint2': actual_joint_state[1]}, protocol=self.protocol)
        self.client.write_points(df, 'encoded_joint_state',
                                 {'joint1': encoded_joint_state[0], 'joint2': encoded_joint_state[1]}, protocol=self.protocol)        
        print("Delete database: " + self.dbname)
        self.client.drop_database(self.dbname)


import rospy
import control_msgs.msg
from control_msgs.msg import JointTrajectoryControllerState
import datetime

class PilzInformer(influx_logging):
    def __init__(self,influx_logger):
        self.diagnostics_sub = rospy.Subscriber('/prbt/manipulator_joint_trajectory_controller/state', JointTrajectoryControllerState, self.diagnostics_callback)
        self.actual_joint_state= ()
        self.influx_logger = influx_logger

    def diagnostics_callback(self, diagnostics):
        self.actual_joint_state= diagnostics.actual.positions
        self.encoded_joint_state=diagnostics.desired.positions
        self.influx_logger.main(self.actual_joint_state,self.encoded_joint_state)
        self.print_informations()
    
    def print_informations(self):
        print self.actual_joint_state




def parse_args():
    """Parse the args from main."""
    parser = argparse.ArgumentParser(
        description='example code to play with InfluxDB')
    parser.add_argument('--host', type=str, required=False,
                        default='localhost',
                        help='hostname of InfluxDB http API')
    parser.add_argument('--port', type=int, required=False, default=8086,
                        help='port of InfluxDB http API')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    influx_logger = influx_logging(host=args.host, port=args.port,user = 'ret',password = 'asdf',dbname = 'demo')
    rospy.init_node("joint_trajectory_subscriber", anonymous=True)
    PilzInformer(influx_logger)
    rospy.spin()