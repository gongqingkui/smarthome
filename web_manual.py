# encoding: utf-8
import web
import os
import sqlite3
import time
from actuatorModule import execute
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
                execute("switcher1",i.switcher1)
        if i.servor1 != "":
            if int(i.servor1)>=0 and int(i.servor1) <=180:
                execute("servor1",i.servor1)
        if i.led1 != "":    
            if i.led1 !="":
                activer("led1",i.led1)
        ''' 
        db1 = db()
        print db1.select("sensors",1 )
        return web.seeother('/')
        '''

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
                'create tableactuators(id integer primary key autoincrement,date text,value text)')
            self.conn.commit()


web.webapi.internalerror = web.debugger                

if __name__ == '__main__':
    app = web.application(urls, globals(),web.reload)
    app.run()
