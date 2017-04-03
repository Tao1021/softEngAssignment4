from flask import Flask, render_template, url_for, request, session, flash, g, jsonify
from functools import wraps
import sys
from flask_mysqldb import MySQLdb
import dbconnect

#create appl object
app = Flask(__name__)

sql = """SELECT DISTINCT
    static.num,
    static.addr,
    DynamicTest.last_update,
    DynamicTest.status,
    static.lat,
    static.longti,
    DynamicTest.available_bikes,
    DynamicTest.available_bike_stands,
    DynamicTest.bike_stands,
    DynamicTest.banking
FROM
    static,
    DynamicTest
WHERE
    static.num = DynamicTest.num
ORDER BY last_update ASC
LIMIT 101;"""

@app.route('/')
def get_mainpage():
    g.db = dbconnect.connection()
    c = g.db.cursor()
    cur = c.execute(sql) 
    rows = c.fetchall()
    dbdata = []
    for eachRow in rows:
        dbdata.append(eachRow)
    c.close()
    g.db.close()
    #return render_template('helloStatic.html', dbdata=dbdata)
    return jsonify(dbdata=dbdata)

if __name__ == '__main__':
        app.run(debug=True)
