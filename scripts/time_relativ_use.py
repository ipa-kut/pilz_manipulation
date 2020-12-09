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
        return True ## the processing is done in the threadEmission, because it is done directly after the robot went out of the area and it is the time there is no socket flow
    else:
        return False
