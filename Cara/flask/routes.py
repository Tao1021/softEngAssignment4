from flask import Flask, render_template, url_for, request, session, flash, g
from functools import wraps
import sys
import sqlite3 as lt


#create appl object
app = Flask(__name__)

app.database = "Dublin_BikesRDB.db"


@app.route('/')
def hello():
        con = lt.connect('dublin_BikesRDB.db')
        g.db = connect_db()
        cur = g.db.execute('select num, Sname, addr, lat, long from Static') #, addr, lat, long from Static')

        dbdata = []
        for row in cur.fetchall():
                dbdata.append(dict(num=row[0], Sname=row[1], addr=row[2], lat=row[3], long=row[4]))

        g.db.close()
        return render_template('helloStatic.html', dbdata=dbdata)
        #return josnify(available=data) #makes data a json obj
        #js respond to event, ajax req to flask appl, get response, return json object, call this funct from js
        #return array or list and send data to google charts
        #write py function and call from js

def connect_db():
        return lt.connect(app.database)

if __name__ == '__main__':
        app.run(debug=True)
