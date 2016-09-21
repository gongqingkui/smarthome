import serial
import os
import sqlite3
import time
from time import sleep

def serialRead():
    t = serial.Serial('/dev/ttyUSB1',9600)
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
            elif s[0]=='F':
                sql = "insert into hcho(date,value) values('%s','%s');"%(time.strftime('%Y-%m-%d %X',time.localtime()),s[2:6])
            if sql!="":
                print sql
                db1.execute(sql)

class db:
    def __init__(self):
        self.db = sqldb()
    def insert(self,table,values):
        return 
    def delete(self,table,index):
        return 
    def update(self,table,index,values):
        return 
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
