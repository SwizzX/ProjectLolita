from common import *


# first date question
def check_q2():
    if user_input.get().lower() == "22/10/2023":
        msg = CTkMessagebox(title="Not bad not bad", message="You remembered!! <3", option_1="Yay")
        response = msg.get()
        if response == "Yay":
            destroy_window(window)
        destroy_window(window)
    elif "10/2023" in user_input.get().lower():
        CTkMessagebox(title="Correct Month", message="you got the month correct but not the date")
    else:
        CTkMessagebox(title="Wrong answer", message=bad_message_list[randint(0, len(bad_message_list) - 1)])


# first qn
window = new_window("Q2", '600x150')

l1 = CTkLabel(window, text="What's the date of the first time we deliberately arranged to hang out? \n"
                           "formatting as dd/mm/yyyy")
user_input = StringVar()
textbox = CTkEntry(window, textvariable=user_input)
b1 = CTkButton(window, command=check_q2, text="I'm confident")  # Remove parentheses
l1.grid(row=0, column=0)
textbox.grid(row=1, column=0)
b1.grid(row=3, column=0)

window.mainloop()
