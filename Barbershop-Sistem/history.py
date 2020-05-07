from tkinter import *
import sqlite3
from window_inserts import window_insert

def history():
    window_history = Tk()
    window_history.title('History')

    def searh_day():
        connection = sqlite3.connect('buy.db')
        c = connection.cursor()
        sqlbarbe1 = c.execute("SELECT SUM(value) FROM service WHERE service='Barber1' and datesday=? and datesmonth=? and datesyear=?",(day.get(),month.get(),year.get()))
        result_barber1['text']=f'Barber 1:R${sqlbarbe1.fetchone()}'

        sqlbarbe2 = c.execute("SELECT SUM(value) FROM service WHERE service='Barber2' and datesday=? and datesmonth=? and datesyear=?",(day.get(),month.get(),year.get()))
        result_barber2['text']=f'Barber 2:R${sqlbarbe2.fetchone()}'

        sqlbar = c.execute("SELECT SUM(value) FROM service WHERE service='Bar' and datesday=? and datesmonth=? and datesyear=?",(day.get(),month.get(),year.get()))
        result_bar['text']=f'Bar:R${sqlbar.fetchone()}'

        sqlproduct = c.execute("SELECT SUM(value) FROM service WHERE service='Product' and datesday=? and datesmonth=? and datesyear=?",(day.get(),month.get(),year.get()))
        result_product['text']=f'Product:R${sqlproduct.fetchone()}'

        sqlexit = c.execute("SELECT SUM(exit) FROM service WHERE service='Exit' and datesday=? and datesmonth=? and datesyear=?",(day.get(),month.get(),year.get()))
        result_exit['text']=f'Exit:R$-{sqlexit.fetchone()}'

        sqltotal = c.execute("SELECT SUM(value) FROM service WHERE datesday=? and datesmonth=? and datesyear=?",(day.get(),month.get(),year.get()))
        result_total['text']=f'Total:R${sqltotal.fetchone()}'

        sqlliquid = c.execute("SELECT SUM(value)-SUM(exit) FROM service WHERE datesday=? and datesmonth=? and datesyear=?",(day.get(),month.get(),year.get()))
        result_liquid['text']=f'Liquid:R${sqlliquid.fetchone()}'
    def searh_month():
        connection = sqlite3.connect('buy.db')
        c = connection.cursor()
        sqlbarbe1 = c.execute("SELECT SUM(value) FROM service WHERE service='Barber1' and datesmonth=? and datesyear=?",(month2.get(),year2.get()))
        result_barber1['text']=f'Barber 1:R${sqlbarbe1.fetchone()}'

        sqlbarbe2 = c.execute("SELECT SUM(value) FROM service WHERE service='Barber2' and datesmonth=? and datesyear=?",(month2.get(),year2.get()))
        result_barber2['text']=f'Barber 2:R${sqlbarbe2.fetchone()}'

        sqlbar = c.execute("SELECT SUM(value) FROM service WHERE service='Bar' and datesmonth=? and datesyear=?",(month2.get(),year2.get()))
        result_bar['text']=f'Bar:R${sqlbar.fetchone()}'

        sqlproduct = c.execute("SELECT SUM(value) FROM service WHERE service='Product' and datesmonth=? and datesyear=?",(month2.get(),year2.get()))
        result_product['text']=f'Product:R${sqlproduct.fetchone()}'

        sqlexit = c.execute("SELECT SUM(exit) FROM service WHERE service='Exit' and datesmonth=? and datesyear=?",(month2.get(),year2.get()))
        result_exit['text']=f'Exit:R$-{sqlexit.fetchone()}'

        sqltotal = c.execute("SELECT SUM(value) FROM service WHERE datesmonth=? and datesyear=?",(month2.get(),year2.get()))
        result_total['text']=f'Total:R${sqltotal.fetchone()}'

        sqlliquid = c.execute("SELECT SUM(value)-SUM(exit) FROM service WHERE datesmonth=? and datesyear=?",(month2.get(),year2.get()))
        result_liquid['text']=f'Liquid:R${sqlliquid.fetchone()}'
    def search_year():
        connection = sqlite3.connect('buy.db')
        c = connection.cursor()
        sqlbarbe1 = c.execute("SELECT SUM(value) FROM service WHERE service='Barber1' and datesyear=?",(year3.get(),))
        result_barber1['text']=f'Barber 1:R${sqlbarbe1.fetchone()}'

        sqlbarbe2 = c.execute("SELECT SUM(value) FROM service WHERE service='Barber2' and datesyear=?",(year3.get(),))
        result_barber2['text']=f'Barber 2:R${sqlbarbe2.fetchone()}'

        sqlbar = c.execute("SELECT SUM(value) FROM service WHERE service='Bar' and datesyear=?",(year3.get(),))
        result_bar['text']=f'Bar:R${sqlbar.fetchone()}'

        sqlproduct = c.execute("SELECT SUM(value) FROM service WHERE service='Product' and datesyear=?",(year3.get(),))
        result_product['text']=f'Product:R${sqlproduct.fetchone()}'

        sqlexit = c.execute("SELECT SUM(exit) FROM service WHERE service='Exit' and datesyear=?",(year3.get(),))
        result_exit['text']=f'Exit:R$-{sqlexit.fetchone()}'

        sqltotal = c.execute("SELECT SUM(value) FROM service WHERE datesyear=?",(year3.get(),))
        result_total['text']=f'Total:R${sqltotal.fetchone()}'

        sqlliquid = c.execute("SELECT SUM(value)-SUM(exit) FROM service WHERE datesyear=?",(year3.get(),))
        result_liquid['text']=f'Liquid:R${sqlliquid.fetchone()}'


    daytext = Label(window_history, text='Day:',
                       font=("Comic Sans MS", "25 "),
                       background='black',
                       foreground='yellow',
                       )
    daytext.place(x=1, y=3)

    day = Entry(window_history,
                width=2,
                bg='white',
                font=('impact bold', '15')
                )
    day.place(x=73, y=15)

    monthtext = Label(window_history,
                      text='Month:',
                       font=("Comic Sans MS", "25 "),
                       background='black',
                       foreground='yellow',
                       )
    monthtext.place(x=150, y=3)

    month= Entry(window_history,
                 width=2,
                 bg='white',
                 font=('impact bold', '15')
                 )
    month.place(x=263, y=15)

    yeartext = Label(window_history, text='Year:',
                       font=("Comic Sans MS", "25 "),
                       background='black',
                       foreground='yellow',
                       )
    yeartext.place(x=350, y=3)

    year = Entry(window_history,
                 width=4,
                 bg='white',
                 font=('impact bold', '15')
                 )
    year.place(x=438, y=15)

    btsearchday = Button(window_history,
                      width=10,
                   text='Search Day',
                   bg='white',
                    bd=10,
                   font=('impact bold', '10'),
                   command=searh_day
                   )
    btsearchday.place(x=500, y=8)

    monthtext2 = Label(window_history,
                      text='Month:',
                       font=("Comic Sans MS", "25 "),
                       background='black',
                       foreground='yellow',
                       )
    monthtext2.place(x=1, y=70)

    month2= Entry(window_history,
                 width=2,
                 bg='white',
                 font=('impact bold', '15')
                 )
    month2.place(x=110, y=85)

    yeartext2 = Label(window_history, text='Year:',
                       font=("Comic Sans MS", "25 "),
                       background='black',
                       foreground='yellow',
                       )
    yeartext2.place(x=170, y=70)

    year2 = Entry(window_history,
                 width=4,
                 bg='white',
                 font=('impact bold', '15')
                 )
    year2.place(x=260, y=85)

    btsearchmonth = Button(window_history,
                      width=10,
                   text='Search Month',
                   bg='white',
                    bd=10,
                   font=('impact bold', '10'),
                   command=searh_month
                   )
    btsearchmonth.place(x=325, y=77)

    yeartext3 = Label(window_history, text='Year:',
                       font=("Comic Sans MS", "25 "),
                       background='black',
                       foreground='yellow',
                       )
    yeartext3.place(x=1, y=130)

    year3 = Entry(window_history,
                 width=4,
                 bg='white',
                 font=('impact bold', '15')
                 )
    year3.place(x=87, y=145)

    btsearchyear = Button(window_history,
                      width=10,
                   text='Search Year',
                   bg='white',
                    bd=10,
                   font=('impact bold', '10'),
                   command=search_year
                   )
    btsearchyear.place(x=150, y=137)

    result_barber1 = Label(window_history, text='BARBER 1:',
                       font=("Comic Sans MS", "25 "),
                       background='black',
                       foreground='yellow',
                       )
    result_barber1.place(x=1, y=200)

    result_barber2 = Label(window_history, text='BARBER 2:',
                       font=("Comic Sans MS", "25 "),
                       background='black',
                       foreground='yellow',
                       )
    result_barber2.place(x=1, y=250)

    result_bar = Label(window_history, text='BAR:',
                       font=("Comic Sans MS", "25 "),
                       background='black',
                       foreground='yellow',
                       )
    result_bar.place(x=1, y=300)

    result_product = Label(window_history, text='Product:',
                       font=("Comic Sans MS", "25 "),
                       background='black',
                       foreground='yellow',
                       )
    result_product.place(x=1, y=350)

    result_exit = Label(window_history, text='Exit:',
                       font=("Comic Sans MS", "25 "),
                       background='black',
                       foreground='red',
                       )
    result_exit.place(x=1, y=400)

    result_total = Label(window_history, text='Total:',
                       font=("Comic Sans MS", "25 "),
                       background='black',
                       foreground='blue',
                       )
    result_total.place(x=1, y=450)

    result_liquid = Label(window_history, text='Liquid:',
                       font=("Comic Sans MS", "25 "),
                       background='black',
                       foreground='powder blue',
                       )
    result_liquid.place(x=1, y=500)

    btinsert = Button(window_history,
                      width=10,
                   text='Insert Values',
                   bg='white',
                    bd=10,
                   font=('impact bold', '10'),
                   command=window_insert
                   )
    btinsert.place(x=100, y=580)

    window_history.configure(background='black')
    window_history.geometry('660x650')
    window_history.mainloop()
