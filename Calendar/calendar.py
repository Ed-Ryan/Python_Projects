import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar

def get_selected_date():
    selected_date = cal.selection_get()
    messagebox.showinfo("Selected Date", f"The selected date is: {selected_date}")

root = tk.Tk()
root.title("GUI Calendar")

cal = Calendar(root, selectmode="day")
cal.pack(pady=20)

select_button = ttk.Button(root, text="Get Selected Date", command=get_selected_date)
select_button.pack(pady=10)

root.mainloop()
