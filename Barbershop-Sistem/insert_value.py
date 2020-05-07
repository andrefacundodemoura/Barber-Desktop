import sqlite3
import datetime
import time

def insert_value(dateday,datemonth,dateyear,service,value,exit):
    times = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%H:%M:%S'))

    connectionall = sqlite3.connect('buy.db')
    c_all= connectionall.cursor()

    c_all.execute("INSERT INTO service (datesday,datesmonth,datesyear,service,value,exit,timestamp) VALUES (?,?,?,?,?,?,?)", (dateday,datemonth,dateyear,service, value,exit,times))

    connectionall.commit()