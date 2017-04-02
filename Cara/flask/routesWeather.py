from flask import Flask, render_template, url_for, request, session, flash, g, jsonify
from functools import wraps
import sys
import sqlite3 as lt
#import dbconnect

#create appl object
app = Flask(__name__)

@app.route('/')
def hello():
    g.db = connect_db()
    c = g.db.execute('select timeStamp, weatherID, temp, desc, icon from weather')
    dbdata = []
    rows = c.fetchall()
    for row in rows:
            dbdata.append(dict(timeStamp=row[0], weatherID=row[1], temp=row[2], desc=row[3], icon=row[4]))
    c.close()
    g.db.close()
    return render_template('helloWeather.html', dbdata=dbdata)


def connect_db():
    app.database = "Dublin_BikesRDB.db"
    return lt.connect(app.database)

if __name__ == '__main__':
        app.run(debug=True)
