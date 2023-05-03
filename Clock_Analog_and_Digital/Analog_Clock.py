import tkinter as tk
import time
import math

def update_clock():
    # Get the current time
    current_time = time.localtime()
    hour = current_time.tm_hour
    minute = current_time.tm_min
    second = current_time.tm_sec
    
    # Calculate the angles of the hands
    hour_angle = math.radians(30 * ((hour % 12) + minute / 60))
    minute_angle = math.radians(6 * minute)
    second_angle = math.radians(6 * second)
    
    # Move the hands to their new positions
    canvas.delete('all')
    draw_clock_face()
    draw_hand(hour_angle, 80, 6)
    draw_hand(minute_angle, 120, 4)
    draw_hand(second_angle, 140, 2)
    
    # Schedule the update_clock function to run again after 1 second
    canvas.after(1000, update_clock)

def draw_clock_face():
    # Draw the clock face
    for i in range(60):
        angle = math.radians(6 * i)
        x1 = 150 + math.sin(angle) * 130
        y1 = 150 - math.cos(angle) * 130
        if i % 5 == 0:
            x2 = 150 + math.sin(angle) * 115
            y2 = 150 - math.cos(angle) * 115
        else:
            x2 = 150 + math.sin(angle) * 125
            y2 = 150 - math.cos(angle) * 125
        canvas.create_line(x1, y1, x2, y2, width=2)
        
def draw_hand(angle, length, width):
    # Draw a clock hand
    x = 150 + math.sin(angle) * length
    y = 150 - math.cos(angle) * length
    canvas.create_line(150, 150, x, y, width=width)

# Create the root window
root = tk.Tk()
root.title("Analog Clock")

# Create a canvas to draw the clock on
canvas = tk.Canvas(root, width=300, height=300, bg='white')
canvas.pack(fill='both', expand=True)

# Call the update_clock function to start the clock
update_clock()

# Run the main loop to display the clock
root.mainloop()
