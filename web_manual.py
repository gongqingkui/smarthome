# encoding: utf-8
import web
import os
import sqlite3
import time
import serial
from actuatorModule import execute
from web import form
# templete floder
render = web.template.render('templates/')

# url tables
urls = ('/', 'index',
        '/manualcontroller', 'manualcontroller',
        '/temperature', 'temperature',
        '/humidity', 'humidity'
        )


class index:
    def GET(self):
        return render.index()

 
class temperature:
    def GET(self):
        db1 = db()
        rs = db1.execute('select * from temperature order by id desc limit 20')
        return render.temperature(rs)


class humidity:
    def GET(self):
        db1 = db()
        rs = db1.execute('select * from humidity order by id desc limit 20')
        return render.humidity(rs)


class manualcontroller:

    def GET(self):
        return web.seeother('/')

    def POST(self):
        i = web.input()
        print i.switcher1, i.servor1, i.led1
        if i.servor1 != "":
            if int(i.servor1)>=0 and int(i.servor1) <=180:
                execute("d",i.servor1)
        elif i.led1 != "":    
            if i.led1 !="":
                execute("s",i.led1)
        elif i.switcher1 != "":
            if i.switcher1 == "1" or i.switcher1 == "0" :
                execute("b",i.switcher1)
        return web.seeother('/')

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
    app = web.application(urls, globals())
    app.run()
