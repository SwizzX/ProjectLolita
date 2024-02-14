from common import *

window = new_window("Congrats!!", '600x150')

l1 = CTkLabel(window, text="You got everything correct! Here's your reward babygirl <3")
b1 = CTkButton(window, command=window.destroy, text="Yayy")
l1.grid(row=0, column=0, padx=60, pady=20)
b1.grid(row=1, column=0)

# window.wait_window(window)  # Use wait_window to wait for the window to be destroyed
window.mainloop()