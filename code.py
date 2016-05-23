# encoding: utf-8
import web
import os
import sqlite3
import time
from web import form
activer = activer()
# templete floder
render = web.template.render('templates/')
# url tables
urls = ('/', 'index',
        '/manualcontroller', 'manualcontroller'
        )


class index:

    def GET(self):
        return render.index()

def activer(name,value):
    print name,value
    return 
class manualcontroller:

    def GET(self):
        return web.seeother('/')

    def POST(self):
        i = web.input()
        print i.switcher1, i.servor1, i.led1
        if i.switcher1 == 1 or i.switcher1 ==0 :
            activer("switcher1",i.switcher1)
            
        if i.servor1>=0 and i.servor1 <=180:
            activer("servor1",i.servor1)
            
        if i.led1 !="":
            activer("led1",i.led1)
        '''
        db = sqldb()
        db.cu.execute('')
        rs = db.cu.fetchall()
        for r in rs:
            print r[0]
        db.conn.commit()
        '''
        return render.seeother('/')

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

                

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
