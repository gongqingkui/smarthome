# encoding: utf-8
import web
import os
import sqlite3
import time
from web import form

# templete floder
render = web.template.render('templates/')

# url tables
urls = ('/', 'index',
        '/manualcontroller', 'manualcontroller'
        )


class index:
    def GET(self):
        return render.index()

class manualcontroller:

    def GET(self):
        return web.seeother('/')

    def POST(self):
        i = web.input()
        print i.switcher1, i.servor1, i.led1
        if i.switcher1 != "":
            if i.switcher1 == "1" or i.switcher1 == "0" :
                activer("switcher1",i.switcher1)
        if i.servor1 != "":
            if int(i.servor1)>=0 and int(i.servor1) <=180:
                activer("servor1",i.servor1)
        if i.led1 != "":    
            if i.led1 !="":
                activer("led1",i.led1)
        
        db1 = db()
        print db1.select("msgs", 3)
        return web.seeother('/')
class db:
    def __init__(self):
        self.db = sqldb()
    def insert(self,table,values):
        return 
    def delete(self,table,id):
        return 
    def update(self,table,id,values):
        return 
    def select(self,table,id):
        self.db.cu.execute('select * from ? where id = ?',('msgs',3))
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
                'create table msgs(id integer primary key,name text,date text,content text)')
            self.cu.execute(
                "insert into msgs values(1,'gong','2016-05-16 16:36:00','hello gong')")
            self.conn.commit()


def activer(name,value):
    print name,value
    serialSend(name,value)
    return 
def serialSend(name,value):
    #serial port init
    #serial send name,value
    return 
                

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
