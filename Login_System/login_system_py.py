import tkinter as tk
from tkinter import *

def IsLoggedIn():
    choose.destroy()
    global login, username_string, password_string
    login = tk.Tk()
    Label(login, text='Enter username: ').grid(row=0, column=0)
    Label(login, text='Enter password: ').grid(row=1, column=0)
    username_string = StringVar(login)
    password_string = StringVar(login)
    username = Entry(login, textvariable = username_string).grid(row=0, column=1)
    password = Entry(login, textvariable = password_string, show='*').grid(row=1, column=1)
    login_BTN = Button(login, text='Submit', command=check_file).grid(row=2, column=0)
    login.mainloop()

def check_file():
    username = username_string.get()
    password = password_string.get()
    login.destroy()
    with open(username + ".txt", "r") as f:
        un = f.readline().strip()
        pw = f.readline().strip()
        if un == username and pw == password:
            global succ
            succ = tk.Tk()
            Label(succ, text='Successful Login!').grid(row=0, column=0)
            succ.after(5000, lambda:succ.destroy())
            succ.mainloop()
        else:
            global fail
            fail = tk.Tk()
            Label(fail, text='Failed log in! Try again...').grid(row=0, column=0)
            fail.after(5000, lambda:fail.destroy())
            fail.after(4900, lambda:main())
            fail.mainloop()

def register():
    choose.destroy()
    global regi, un_string, pw_string
    regi = tk.Tk()
    Label(regi, text = 'Username:').grid(row=0, column=0)
    Label(regi, text = 'Password:').grid(row=1, column=0)
    un_string = StringVar(regi)
    pw_string = StringVar(regi)
    un = Entry(regi, textvariable=un_string).grid(row=0, column=1)
    pw = Entry(regi, textvariable = pw_string, show = '*').grid(row=1, column=1)
    reg_BTN = Button(regi, text="Submit", command=write_file).grid(row=2, column=0)
    regi.mainloop()


def write_file():
    user = un_string.get()
    word = pw_string.get()
    regi.destroy()
    print(user)
    print(word)
    with open(user +".txt", "w") as f:
        f.write(user + "\n" + word)
    main()
    
def main():
    global choose
    choose = tk.Tk()
    reg = Button(choose, text = "Register New User", command=register).grid(row=0,column=0)
    log = Button(choose, text = "Log In", command=IsLoggedIn).grid(row=1, column=0)
    choose.mainloop()

def end():
    succ.destroy()
    
main()