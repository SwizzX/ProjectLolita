from common import *


def check_name():
    if user_input.get().lower() == "trincakes" or user_input.get().lower() == "julianne":
        msg = CTkMessagebox(title="Let's play a guessing game", message="Very well, you may proceed", option_1="Ok")
        response = msg.get()
        if response == "Yes":
            destroy_window(window)
        destroy_window(window)
    elif user_input.get().lower() == "sean":
        CTkMessagebox(title="Still miss me huh?", message="Why are you trying my name??? bad girls get punished when "
                                                          "they break the rules")
    else:
        CTkMessagebox(title="Wrong recipient", message="Error: message meant only for Julianne")


# name prompt window
window = new_window("Hi, what's your name?", '400x150')

user_input = StringVar()
textbox = CTkEntry(window, textvariable=user_input)
textbox.grid(row=0, column=0, padx=125, pady=30)
b1 = CTkButton(window, command=check_name, text="Submit")
b1.grid(row=1, column=0)

# window.wait_window(window)  # Use wait_window to wait for the window to be destroyed
window.mainloop()

# game start window
window = new_window("Are you ready?", '600x150')

l1 = CTkLabel(window, text="If you can answer all these questions correctly, there's a surprise for you at the end :)")
b1 = CTkButton(window, command=window.destroy, text="Let's do this")
l1.grid(row=0, column=0, padx=60, pady=20)
b1.grid(row=1, column=0)

# window.wait_window(window)  # Use wait_window to wait for the window to be destroyed
window.mainloop()
