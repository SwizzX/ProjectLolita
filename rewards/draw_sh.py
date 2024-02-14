import tkinter as tk
from random import *


def draw_knife_mark():
    start_x = randint(0, 300)
    start_y = randint(0, 600)
    end_x = randint(0, 300)
    end_y = randint(0, 600)
    canvas.create_line(start_x, start_y, end_x, end_y, fill="red", width=2)


# Create the main window
root = tk.Tk()
root.title("Sean's arm")

# Create a canvas with a skin-toned background
canvas = tk.Canvas(root, width=300, height=600, bg="#ffdab9")  # You can adjust the background color as needed
canvas.pack()

# Create a button to draw the knife mark
button = tk.Button(root, text="hurt me", command=draw_knife_mark)
button.pack()

# Run the main event loop
root.mainloop()
