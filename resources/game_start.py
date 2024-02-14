from common import *

# game start window
window = new_window("Are you ready?", '600x150')

l1 = CTkLabel(window, text="If you can answer all these questions correctly, there's a surprise for you at the end :)")
b1 = CTkButton(window, command=window.destroy, text="Let's do this")
l1.grid(row=0, column=0, padx=60, pady=20)
b1.grid(row=1, column=0)

# window.wait_window(window)  # Use wait_window to wait for the window to be destroyed
window.mainloop()
print("game_start.py terminated")
