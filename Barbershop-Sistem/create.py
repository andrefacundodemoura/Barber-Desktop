import sqlite3

def create_db():
    connectionall = sqlite3.connect('buy.db')
    c_all = connectionall.cursor()
    c_all.execute('CREATE TABLE IF NOT EXISTS service(datesday text,datesmonth text,datesyear text,service text,value real,exit real,timestamp text)')
    connectionall.commit()
