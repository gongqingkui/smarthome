import serial
import os
import sqlite3
import time
from time import sleep
import json
import urllib2
import time
import random

def toYeeLink(sensorId,value):
    apikey = 'b6984ebdde615e36eda3c7420e4a422b'
    sensorURL = 'http://api.yeelink.net/v1.0/device/350986/sensor/%s/datapoints'%sensorId
    print sensorURL
    timeFormat = '%Y-%m-%dT%X'
    timeString = time.strftime(timeFormat,time.localtime())
    values = {'timestamp':timeString,'value':value}
    jdata = json.dumps(values)
    print jdata

    r = urllib2.Request(sensorURL,jdata)
    r.add_header('U-ApiKey',apikey)

    resp = urllib2.urlopen(r)
    time.sleep(30)

def serialRead():
    t = serial.Serial('/dev/ttyUSB1',9600)
    print t.isOpen()
    with t:
        while(1):
            s = t.readline()
            if s[0]=='T':
                toYeeLink(394220,s[2:6]) 
            elif s[0]=='H':
                toYeeLink(394218,s[2:6]) 
            elif s[0]=='F':
                pass

if __name__ == '__main__':
    while(True):
        serialRead()
