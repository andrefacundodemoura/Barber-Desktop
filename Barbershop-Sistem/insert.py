import sqlite3
import datetime
import time

def insert_db(service,value,exit):
    dateday = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%d'))
    datemonth = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%m'))
    dateyear = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y'))
    times = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%H:%M:%S'))

    connectionall = sqlite3.connect('buy.db')
    c_all= connectionall.cursor()

    c_all.execute("INSERT INTO service (datesday,datesmonth,datesyear,service,value,exit,timestamp) VALUES (?,?,?,?,?,?,?)", (dateday,datemonth,dateyear,service, value,exit,times))

    connectionall.commit()
