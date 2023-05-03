import tkinter as tk
import time

def update_clock():
    # Get the current time and format it
    current_time = time.strftime('%H:%M:%S')
    
    # Update the clock label text
    clock_label.config(text=current_time)
    
    # Schedule the update_clock function to run again after 1 second
    clock_label.after(1000, update_clock)

# Create the root window
root = tk.Tk()
root.title("Clock")

# Create a label to display the clock
clock_label = tk.Label(root, font=('Arial', 50), bg='white', fg='black')
clock_label.pack(fill='both', expand=True)

# Call the update_clock function to start the clock
update_clock()

# Run the main loop to display the clock
root.mainloop()
