from tkinter import *
from insert_value import insert_value
from window_confirm import window_confirm


def window_insert():
    window = Tk()
    window.title('Insert')

    def barber1():
        insert_value(day.get(),month.get(),year.get(),'Barber1', valueinput.get(), 0)
        valueinput.delete(0, END)
        window_confirm('Barber1')

    def barber2():
        insert_value(day.get(),month.get(),year.get(),'Barber2', valueinput.get(), 0)
        valueinput.delete(0, END)
        window_confirm('Barber2')

    def bar():
        insert_value(day.get(),month.get(),year.get(),'Bar', valueinput.get(), 0)
        valueinput.delete(0, END)
        window_confirm('Bar')

    def product():
        insert_value(day.get(),month.get(),year.get(),'Product', valueinput.get(), 0)
        valueinput.delete(0, END)
        window_confirm('Product')

    def exit():
        insert_value(day.get(),month.get(),year.get(),'Exit', 0, valueinput.get())
        valueinput.delete(0, END)
        window_confirm('Exit')

    daytext = Label(window, text='Day:',
                       font=("Comic Sans MS", "25 "),
                       background='red',
                       foreground='yellow',
                       )
    daytext.place(x=1, y=3)

    day = Entry(window,
                width=2,
                bg='white',
                font=('impact bold', '15')
                )
    day.place(x=73, y=15)

    monthtext = Label(window,
                      text='Month:',
                       font=("Comic Sans MS", "25 "),
                       background='red',
                       foreground='yellow',
                       )
    monthtext.place(x=150, y=3)

    month= Entry(window,
                 width=2,
                 bg='white',
                 font=('impact bold', '15')
                 )
    month.place(x=263, y=15)

    yeartext = Label(window, text='Year:',
                       font=("Comic Sans MS", "25 "),
                       background='red',
                       foreground='yellow',
                       )
    yeartext.place(x=350, y=3)

    year = Entry(window,
                 width=4,
                 bg='white',
                 font=('impact bold', '15')
                 )
    year.place(x=438, y=15)

    # entrada
    value = Label(window, text='Value:$',
                  font=("Comic Sans MS", "40 "),
                  background='red',
                  foreground='yellow',
                  )
    value.place(x=250, y=100)

    valueinput = Entry(window,
                       width=10,
                       bd=8,
                       bg='powder blue',
                       font=('impact bold', '25')
                       )
    valueinput.place(x=470, y=120)

    # Buttons
    barber1 = Button(window,
                     text='Barber1',
                     bg='powder blue',
                     bd=10,
                     font=('impact bold', '20'),
                     command=barber1
                     )
    barber1.place(x=357, y=350)

    barber2 = Button(window,
                     text='Barber2',
                     bg='powder blue',
                     bd=10,
                     font=('impact bold', '20'),
                     command=barber2
                     )
    barber2.place(x=495, y=350)

    bar = Button(window,
                 text='Bar',
                 bg='powder blue',
                 bd=10,
                 font=('impact bold', '20'),
                 command=bar
                 )
    bar.place(x=632, y=350)

    product = Button(window,
                     text='Product',
                     bg='powder blue',
                     bd=10,
                     font=('impact bold', '20'),
                     command=product
                     )
    product.place(x=714, y=350)

    exit = Button(window,
                  text='Exit',
                  bg='red',
                  bd=10,
                  font=('impact bold', '20'),
                  command=exit
                  )
    exit.place(x=848, y=350)

    window.configure(background='red')
    window.geometry('1000x800')
    window.mainloop()



