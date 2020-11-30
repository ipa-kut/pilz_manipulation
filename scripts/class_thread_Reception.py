#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 16:25:14 2020

@author: ret
"""

import socket, sys, threading
import csv
import time

class ThreadReception(threading.Thread):
    """objet thread gérant la réception des messages"""
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn           # réf. du socket de connexion
        self.data = []
        
    def run(self):
        while 1:
            message_recu = self.connexion.recv(1024)
            self.data.append([message_recu])
            print "*" + message_recu + "*"
            #print self.data 
            if message_recu =='' or message_recu.upper() == "FIN":
                self._Thread__stop()
                print('the thread is stopped')
                break
        print "Client stopped. Connection end."
        self.connexion.close()