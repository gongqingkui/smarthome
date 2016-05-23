# encoding: utf-8
import web,os,sqlite3,time
from web import form
#templete floder
render = web.template.render('templates/')
#url tables
urls = ('/', 'index',
    )


class index:
    def GET(self):
        return render.index()
'''
#get or post -> function
class delete:
    #GET function
    def GET(self):
        # url eg. http://192.168.1.3:1234/delete?id=1
        i = web.input(id=None)
        #db
        sdb = sqldb()
        sdb.cu.execute('delete from msgs where id = ?', i.id)
        sdb.conn.commit()
        #go to /viewPost page
        return web.seeother('/viewPost')


class edit:
    #POST function
    def POST(self):
        #the form is i
        i = web.input()
        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        sdb = sqldb()
        i = (i.name, i.content, i.id)
        rec = sdb.cu.execute(
            'update msgs set name = ?,content= ? where id = ?', i)
        sdb.conn.commit()
        return web.seeother('/viewPost')

    def GET(self):
        return web.seeother('/')


class new:
    def POST(self):
        i = web.input()
        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        sdb = sqldb()
        rec = sdb.cu.execute('select * from msgs')
        dbre = sdb.cu.fetchall()
        for k in dbre:
            j = k[0] + 1

        t = (j, i.name, date, i.content)
        print t
        sdb.cu.execute('insert into msgs values(?,?,?,?)', t)
        sdb.conn.commit()
        return web.seeother('/viewPost')

    def GET(self):
        return web.seeother('/')


class newPost:
    def GET(self):
        return render.newPost()


class editPost:
    def GET(self):
        i = web.input()
        sdb = sqldb()
        rec = sdb.cu.execute('select * from msgs where id = ?', i.id)
        dbre = sdb.cu.fetchall()
        return render.editPost(dbre)


class viewPost:
    def GET(self):
        sdb = sqldb()
        rec = sdb.cu.execute('select * from msgs')
        dbre = sdb.cu.fetchall()
        return render.viewPost(dbre)
'''

class sqldb:
    def __init__(self):
        if os.path.exists('msg.db'):
            self.conn = sqlite3.connect('msg.db')
            self.cu = self.conn.cursor()
        else:
            self.conn = sqlite3.connect('msg.db')
            self.cu = self.conn.cursor()
            self.cu.execute('create table msgs(id integer primary key,name text,date text,content text)')
            self.cu.execute("insert into msgs values(1,'gong','2016-05-16 16:36:00','hello gong')")
            self.conn.commit()


if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
