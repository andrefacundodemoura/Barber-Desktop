from tkinter import *
from user import user
import sqlite3
from insert import insert_db
from create import create_db
from window_confirm import window_confirm
window1 = Tk()
window1.title('BARBER SHOP')

def buy():
    connection = sqlite3.connect('buy.db')
    c = connection.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS buy(value real)')

    c.execute("INSERT INTO buy (value) VALUES (?)", (valueinput.get(),))

    connection.commit()

def new():
    connection = sqlite3.connect('buy.db')
    c = connection.cursor()

    sql = c.execute('SELECT SUM(value) FROM buy ')
    result['text'] = f'Total:${sql.fetchone()}'

    c.execute('DELETE FROM buy WHERE value')
    connection.commit()

def barber1():
    create_db()
    insert_db('Barber1',valueinput.get(),0)
    valueinput.delete(0, END)
    window_confirm('Barber1')



def barber2():
    create_db()
    insert_db('Barber2',valueinput.get(),0)
    valueinput.delete(0, END)
    window_confirm('Barber2')


def bar():
    create_db()
    insert_db('Bar',valueinput.get(),0)
    valueinput.delete(0, END)
    window_confirm('Bar')

def product():
    create_db()
    insert_db('Product',valueinput.get(),0)
    valueinput.delete(0, END)
    window_confirm('Product')

def exit():
    create_db()
    insert_db('Exit',0,valueinput.get())
    valueinput.delete(0, END)
    window_confirm('Exit')

# texto inicial
barbershop = Label(window1, text='Barber Shop',
                   font=("Comic Sans MS", "50 "),
                   background='black',
                   foreground='yellow',
                   )
barbershop.place(x=450, y=1)

# entrada
value = Label(window1, text='Value:$',
              font=("Comic Sans MS", "40 "),
              background='black',
              foreground='yellow',
              )
value.place(x=250, y=100)

valueinput = Entry(window1,
                   width=10,
                   bd=8,
                   bg='powder blue',
                   font=('impact bold', '25')
                   )
valueinput.place(x=470, y=120)

result = Label(window1, text='Total:$',
               font=("Comic Sans MS", "40 "),
               background='black',
               foreground='red',
               )
result.place(x=450, y=220)

#Buttons
barber1 = Button(window1,
                 text='Barber1',
                 bg='powder blue',
                 bd=10,
                 font=('impact bold', '20'),
                 command=barber1
                 )
barber1.place(x=357, y=350)

barber2 = Button(window1,
                 text='Barber2',
                 bg='powder blue',
                 bd=10,
                 font=('impact bold', '20'),
                 command=barber2
                 )
barber2.place(x=495, y=350)

bar = Button(window1,
             text='Bar',
             bg='powder blue',
             bd=10,
             font=('impact bold', '20'),
             command=bar
             )
bar.place(x=632, y=350)

product = Button(window1,
                 text='Product',
                 bg='powder blue',
                 bd=10,
                 font=('impact bold', '20'),
                 command=product
                 )
product.place(x=714, y=350)

exit = Button(window1,
              text='Exit',
              bg='red',
              bd=10,
              font=('impact bold', '20'),
              command=exit
              )
exit.place(x=848, y=350)


btbuy = Button(window1, width=10,
               text='Buy',
               bg='white',
               bd=10,
               font=('impact bold', '16'),
               command=buy
               )
btbuy.place(x=685, y=120)

btnew = Button(window1, width=10,
               text='end',
               bg='white',
               bd=10,
               font=('impact bold', '16'),
               command=new
               )
btnew.place(x=840, y=120)



bthistotory = Button(window1, width=10,
                     text='History',
                     bg='white',
                     bd=10,
                     font=('impact bold', '25'),
                     command=user
                     )
bthistotory.place(x=550, y=550)

window1.configure(background='black')
window1.geometry('1350x800')
window1.mainloop()
