#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 16:15:23 2020

@author: ret
"""

import datetime
t0=datetime.datetime.utcnow()

time_t1=t0
time_t1_plus_delta_t = t0
time_t2=t0
time_zero = datetime.timedelta(0, 0, 0)
Btn_Using = "" # we are using this bool to know what we are using "Btn1" or "Btn2"

def compare_time():
    if (time_t1_plus_delta_t - time_t1 > time_zero and time_t1_plus_delta_t - time_t2 < time_zero) :    
        return True
    else:
        print("time_relativ_use.time_t1_plus_delta_t = ", time_t1_plus_delta_t)
        print("time_relativ_use.time_t1 = ", time_t1)
        print("time_relativ_use.time_t2 = ", time_t2)
        return False
#list_all_info = []
#list_error_info = []
#info_from_socket = "" #"datetime"+ ";" + "pressed"
#info_from_robot = "" #"datetime" + ";" +"in/out of the area"
#
#def csv_all_info():
#    '''return in a way to get the logged file in csv '''
#    pass
#
#def csv_error_info():
#    '''return in a way to get the logged of the error in csv '''
#    pass
#def define_list_all_info():
#    '''split the information from csv_all_info '''
#    return list_all_info 
#
#def define_list_error_info():
#    '''split the csv_error_info '''
#    return list_error_info 