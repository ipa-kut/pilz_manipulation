#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 16:25:14 2020

@author: ret
"""

import socket, sys, threading
import csv
import time
import datetime
import time_relativ_use
import write_influxdb


class ThreadReception(threading.Thread):
    """objet thread gérant la réception des messages"""
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn           # réf. du socket de connexion
        self.data = []
        
        
    def run(self):
        while 1:
            message_recu = self.connexion.recv(1024)
            print "*" + message_recu + "*"
            try:
                write_influxdb.list_msg = message_recu.split(";")
                time_relativ_use.time_t1_plus_delta_t = datetime.datetime.strptime(write_influxdb.list_msg[0], '%Y-%m-%d %H:%M:%S.%f')
                if write_influxdb.list_msg[1] == "Btn1" : ## checking the name of the Btn
                    write_influxdb.list_msg  = [write_influxdb.list_msg[0],True,False,True,False]
                    write_influxdb.list_error= [write_influxdb.list_msg[0],True,False,True]
                if write_influxdb.list_msg[1] == "Btn2" : 
                    write_influxdb.list_msg  = [write_influxdb.list_msg[0],False,True,False,True]
                    write_influxdb.list_error= [write_influxdb.list_msg[0],False,True,True]
            except:
                pass
            #print self.data 
            if message_recu =='' or message_recu.upper() == "FIN":
                self._Thread__stop()
                print('the thread is stopped')
                break
        print "Client stopped. Connection end."
        self.connexion.close()