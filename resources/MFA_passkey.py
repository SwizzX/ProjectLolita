from common import *


# validating the program is actually being run by julianne
def check_passkey():
    if user_input.get() == "314159":
        msg = CTkMessagebox(title="Let's play a guessing game", message="Very well, you may proceed", option_1="Ok")
        response = msg.get()
        if response == "Ok":
            destroy_window(window)
        destroy_window(window)
    else:
        CTkMessagebox(title="Wrong recipient", message="Error: message meant only for Julianne")


# name prompt window
window = new_window("What's your phone passkey?", '400x150')

user_input = StringVar()
textbox = CTkEntry(window, textvariable=user_input)
textbox.grid(row=0, column=0, padx=125, pady=30)
b1 = CTkButton(window, command=check_passkey, text="Submit")
b1.grid(row=1, column=0)

# window.wait_window(window)  # Use wait_window to wait for the window to be destroyed
window.mainloop()
print("MFA_passkey.py terminated")
