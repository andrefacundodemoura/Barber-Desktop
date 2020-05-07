from tkinter import *
from history import history

def user():
    windowuser = Tk()
    windowuser.title('User')
    def verification():
        loginok = logininput.get()
        passwordok = passwordinput.get()
        if loginok == 'admin' and passwordok == 'admin':
            passwordinput.delete(0, END)
            logininput.delete(0,END)
            history()

        else:
            passwordinput.delete(0, END)
            logininput.delete(0, END)
            error['text'] = 'Access Denied'

        passwordinput.delete(0, END)
    login = Label(windowuser, text='Login',
                  font=("Comic Sans MS", "15 "),
                  background='grey',
                  foreground='yellow',
                  )
    login.place(x=70, y=50)

    logininput = Entry(windowuser,
                       width=10,
                       bg='powder blue',
                       bd=10,
                       font=('impact bold', '12')
                       )
    logininput.place(x=130, y=50)


    password = Label(windowuser, text='Password',
                  font=("Comic Sans MS", "15 "),
                  background='grey',
                  foreground='yellow',
                  )
    password.place(x=35, y=100)


    passwordinput = Entry(windowuser,
                          width=10,
                          bg='powder blue',
                          bd=10,
                          font=('impact bold', '12')
                          )
    passwordinput.place(x=130, y=100)
    btenter = Button(windowuser, text='Enter',
                     bg='powder blue',
                     bd=10,
                     font=('impact bold', '15'),
                     command=verification
                     )

    btenter.place(x=100, y=150)

    error = Label(windowuser, text='',
                  font=("Comic Sans MS", "15 "),
                  background='grey',
                  foreground='red',
                  )
    error.place(x=80, y=200)



    windowuser.configure(background='grey')
    windowuser.geometry('300x250')
    windowuser.mainloop()


