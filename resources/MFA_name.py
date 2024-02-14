from common import *


# validating the program is actually being run by julianne
def check_name():
    if user_input.get().lower() == "trincakes" or user_input.get().lower() == "julianne":
        msg = CTkMessagebox(title="Identity validated", message="Please input your phone password next.", option_1="Ok")
        response = msg.get()
        if response == "Yes":
            destroy_window(window)
        destroy_window(window)
    elif user_input.get().lower() == "sean":
        CTkMessagebox(title="Still miss me huh?", message="Why are you trying my name??? bad girls get punished when "
                                                          "they break the rules")
    else:
        CTkMessagebox(title="Wrong recipient", message="Error: message meant only for Julianne")


def check_passkey():
    if user_input.get().lower() == "314159":
        msg = CTkMessagebox(title="Let's play a guessing game", message="Very well, you may proceed", option_1="Ok")
        response = msg.get()
        if response == "Yes":
            destroy_window(window)
        destroy_window(window)
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
print("MFA_name.py terminated")
