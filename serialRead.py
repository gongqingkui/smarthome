import serial
import os
import sqlite3
import time
from time import sleep 
import json
import urllib2
import random

def serialRead():
    t = serial.Serial('/dev/ttyUSB0',9600)
    print t.isOpen()
    db1 = db()
    with t:
        while(1):
            s = t.readline()
            print s
            sql =""
            if s[0]=='T':
                sql = "insert into temperature (date,value) values('%s','%s');"%(time.strftime('%Y-%m-%d %X',time.localtime()),s[2:6])
            elif s[0]=='H':
                sql = "insert into humidity (date,value) values('%s','%s');"%(time.strftime('%Y-%m-%d %X',time.localtime()),s[2:6])
            elif s[0]=='C':
                sql = "insert into hcho(date,value) values('%s','%s');"%(time.strftime('%Y-%m-%d %X',time.localtime()),s[2:6])
            if sql!="":
                print sql
                db1.execute(sql)
            newDataToYeeLink()
            time.sleep(30)
             
def newDataToYeeLink():

    i = random.randint(1,3)
    print i
    if i == 1:
        r = newData('hcho')
        toYeeLink(395037,r[0][1],r[0][2])
    elif i == 2:
        r = newData('temperature')
        toYeeLink(394220,r[0][1],r[0][2])
    elif i == 3:
        r = newData('humidity')
        toYeeLink(394218,r[0][1],r[0][2])
       
def newData(table):
    db2 = db()
    return db2.selectNew(table) 
    db2.close()
class db:
    def __init__(self):
        self.db = sqldb()
    def close(self):
        self.db.conn.close()
    def insert(self,table,values):
        return 
    def delete(self,table,index):
        return 
    def update(self,table,index,values):
        return 
    def selectNew(self,table):
        sql = 'select * from %s order by id desc limit 1'%(table)
        self.db.cu.execute(sql)
        rs = self.db.cu.fetchall()
        self.db.conn.commit()
        return rs
    def select(self,table,index):
        i = (table,index)
        sql = 'select * from %s where id = %d'%(table,index)
        self.db.cu.execute(sql)
        rs = self.db.cu.fetchall()
        self.db.conn.commit()
        return rs
    def execute(self,sql):
        self.db.cu.execute(sql)
        rs = self.db.cu.fetchall()
        self.db.conn.commit()
        return rs
    
    
def toYeeLink(sensorId,t,value):
    apikey = 'b6984ebdde615e36eda3c7420e4a422b'
    sensorURL = 'http://api.yeelink.net/v1.0/device/350986/sensor/%s/datapoints'%sensorId
    print sensorURL
    timeFormat = '%Y-%m-%dT%X'
    timeString = time.strftime(timeFormat,time.localtime())
    #values = {'timestamp':timeString,'value':value}
    values = {'timestamp':t,'value':value}
    jdata = json.dumps(values)
    print jdata

    r = urllib2.Request(sensorURL,jdata)
    r.add_header('U-ApiKey',apikey)

    try:
        resp = urllib2.urlopen(r)
    except Exception,e:
        print Exception,":",e


class sqldb:

    def __init__(self):
        self.db = 'db.db'
        if os.path.exists(self.db):
            self.conn = sqlite3.connect(self.db)
            self.cu = self.conn.cursor()
        else:
            self.conn = sqlite3.connect(self.db)
            self.cu = self.conn.cursor()
            self.cu.execute(
                'create table sensors(id integer primary key autoincrement,date text,value text)')
            self.cu.execute(
                'insert into sensors values(null,\'2016-1-1 12:00:00\',\'32\')')
            self.cu.execute(
                'create table actuators(id integer primary key autoincrement,date text,value text)')
            self.cu.execute(
                'insert into actuators values(null,\'2016-1-1 12:00:02\',\'open AC ato 26\')')
            self.conn.commit()

if __name__ == '__main__':
    serialRead()
