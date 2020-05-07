from tkinter import *

def window_confirm(service):
    window = Tk()
    window.title('Confirm')

    confirm = Label(window, text=f'Value registered for {service} successfully',
                   font=("Comic Sans MS", "12 "),
                   background='white',
                   foreground='red',
                   )
    confirm.place(x=5, y=30)

    window.configure(background='white')
    window.geometry('350x100')
    window.mainloop()
