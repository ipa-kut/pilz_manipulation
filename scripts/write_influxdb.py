#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 15:01:07 2020

@author: ret
"""


from influxdb import InfluxDBClient
import datetime

'''
From BtnDefinition I find which Port I am using and how to use them afterwards
'''

###
'''
creation of the DB
'''

list_msg = []
list_error=[]
def write_into_db():
    client=InfluxDBClient(host="localhost",port="8086")
    client.create_database('BtnMasherApplication_DB_computer_Test_v1') ## Always writing in the same DB for now
    print(client.get_list_database())   ## This will be useful to chose the name of the database for each test
    client.switch_database('BtnMasherApplication_DB_computer_Test_v1')
    return client

''' Every time we have an information we are gonna write it in the  '''
def json_body_define_allInfo(list_all_info): # Add a parameter in order to change the name of the measurement for different test
    #if PushBtn_Port == BtnDefinition.PushBtn1_Port:
    ''' First possibility of information '''
    json_body = [
        {
            "measurement": "Ret_Test_v3",
            "tags": {
                "requestName": "All_Information",
                "requestType": "GET"
            },
            "time":list_all_info[0],#datetime.datetime.utcnow(),
             "fields": {
                "EndEffectorIn_Btn1_Area": list_all_info[1], # Boolean: True or False
                "EndEffectorIn_Btn2_Area": list_all_info[2], # Boolean: True or False
                "Btn1_Pressed": list_all_info[3], #Boolean True or False
                "Btn2_Pressed": list_all_info[4] #Boolean True or False
                        }
        }
    ]
    return json_body

def json_body_define_errorInfo(list_error_info): # Add a parameter in order to change the name of the measurement for different test
    #if PushBtn_Port == BtnDefinition.PushBtn1_Port:
    ''' First possibility of information '''
    json_body = [
        {
            "measurement": "Ret_Test_v2",
            "tags": {
                "requestName": "Error_Information",
                "requestType": "GET"
            },
            "time":list_error_info[0],
             "fields": {
                "Btn1_Pressed": list_error_info[1], # Boolean: True or False
                "Btn2_Pressed": list_error_info[2], # Boolean: True or False
                "Btn_Pressed_Out_Of_Time_Interval" : list_error_info[3]
                        }
        }
    ]
    return json_body

def write_data(data,client):
    client.write_points(data)

