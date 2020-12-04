#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:00:18 2020

@author: ret
"""

import csv
import datetime

name_file = "/home/ret/workspaces/ret/src/pilz_manipulation/scripts/csv_log_ret/test.csv"
header = ['datetime.utcnow','Btn1_Pressed','Btn2_Pressed','EndEffectoreIn_Btn1_Area','EndEffectorIn_Btn2_Area']

def create_csv_file(header,name_file): # to use if we want to have a new csv file for every test we run
    f_ret = open (name_file, 'aw')
    writer = csv.writer(f_ret,delimiter=',')
    writer.writerow(header)
    return name_file



def write_into_csv(name_file,row_to_add):
    f_ret = open (name_file, 'aw')
    writer = csv.writer(f_ret,delimiter=',')
    writer.writerow(row_to_add)