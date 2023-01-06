import tkinter as tk
from tkinter import *

def submit():
    heading = tk.Label(master, text="Questionaire", font=('Helvetica', 20)).grid(row=0)
    first1 = tk.Label(master, text="First name:").grid(row=1,column=0)
    first2 = tk.Entry(master, width=40).grid(row=1,column=1)
    last1 = tk.Label(master, text="Last name:").grid(row=2,column=0)
    last2 = tk.Entry(master, width=40).grid(row=2,column=1)
    email1 = tk.Label(master, text="Email:").grid(row=3,column=0)
    email2 = tk.Entry(master, width=40).grid(row=3,column=1)
    tele1 = tk.Label(master, text="Telephone Number:").grid(row=4,column=0)
    tele2 = tk.Entry(master, width=40).grid(row=4,column=1)
    birth1 = tk.Label(master, text="When is your birthday:").grid(row=5,column=0)
    birth2 = birthdate()
    age1 = tk.Label(master, text="How old are you:").grid(row=6,column=0)
    age2 = age()
    volume1 = tk.Label(master, text="What is your volume currently at:").grid(row=7,column=0)
    volume = tk.Scale(master, from_=0, to=100, orient=tk.HORIZONTAL).grid(row=7, column=1)
    gender1 = tk.Label(master, text="What gender do you identify as:").grid(row=8,column=0)
    gender2 = gender()
    education1 = tk.Label(master, text="What describes your level of education:").grid(row=9,column=0)
    education2 = edu()
    fav1 = tk.Label(master, text="Your favorite thing for dinner is:").grid(row=15,column=0)
    fav2 = tk.Entry(master, width=40).grid(row=15,column=1)
    vacation1 = tk.Label(master, text="What would your ideal vacation be:").grid(row=16,column=0)
    vacation2 = vaca()
    comment1 = tk.Label(master, text="Comments:").grid(row=17,column=0)
    comment2 = Text(master, height=5,width=50).grid(row=17, column = 1)
    submitButton = Button(master, text="Submit", command=toFile).grid(row=18,column=1)
    
def birthdate():
    bday_month = StringVar()
    bday_day = StringVar()
    bday_year = StringVar()
    month_list = ['January','February','March','April','May','June','July','August','September','October','November','December']
    opt_month = OptionMenu(master, bday_month, *month_list)
    opt_month.grid(row = 5, column = 1)
    opt_day = OptionMenu(master, bday_day, *[i for i in range(1,32)])
    opt_day.grid(row = 5, column = 2)
    opt_year = OptionMenu(master, bday_year, *[i for i in range(1970,2021)])
    opt_year.grid(row = 5, column = 3)
    
def age():
    age = StringVar()
    pick_age = OptionMenu(master, age, *[i for i in range(1,100)])
    pick_age.grid(row = 6, column = 1)
    

def gender():
    gend = StringVar()
    gend_list = ["Man","Woman","Transgender","Non-Binary","Prefer not to say", "Other"]
    pick_gend = OptionMenu(master, gend, *gend_list)
    pick_gend.grid(row=8, column=1)

def edu():
    var1 = tk.IntVar()
    tk.Checkbutton(master, text="High School", variable=var1).grid(row=9, column=1)
    var2 = tk.IntVar()
    tk.Checkbutton(master, text="Some College", variable=var2).grid(row=10, column=1)
    var3 = tk.IntVar()
    tk.Checkbutton(master, text="Associates", variable=var3).grid(row=11, column=1)
    var4 = tk.IntVar()
    tk.Checkbutton(master, text="Bachelors", variable=var4).grid(row=12, column=1)
    var5 = tk.IntVar()
    tk.Checkbutton(master, text="Masters", variable=var5).grid(row=13, column=1)
    var6 = tk.IntVar()
    tk.Checkbutton(master, text="PHd", variable=var6).grid(row=14, column=1)
    
def vaca():
    select = StringVar()
    select_list = ["Beach","Stay at home","Destination Vacation","Other"]
    pick_select = OptionMenu(master, select, *select_list)
    pick_select.grid(row=16, column=1)
    
def toFile():
    try:
        with open('data.txt', 'w') as file:
            file.write(f'First name: {first2}\n')
            file.write(f'Last name: {last2}\n')
            file.write(f'Email: {email2}\n')
            file.write(f'Telephone Number: {tele2}\n')
            file.write(f'Birthdate: {birth2}\n')
            file.write(f'Age: {age()}\n')
            file.write(f'Volume currently: {volume}\n')
            file.write(f'Gender: {gender()}\n')
            file.write(f'Level of Education: {edu()}\n')
            file.write(f'Favorite thing for dinner: {fav2}\n')
            file.write(f'Ideal vacation: {vaca()}\n')
            file.write(f'Comments: {comment2}\n')
        print('Data collected successfully!')
    except:
        print('Error collecting data!')
    
master = tk.Tk()
master.geometry("1000x1000")
submit()
master.mainloop()