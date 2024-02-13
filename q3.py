from common import *


def check_q1():
    if user_input.get().lower() == "5":
        msg = CTkMessagebox(title="And so many more since", message="The start of my downfall",
                            option_1="You're pathetic")
        response = msg.get()
        if response == "You're pathetic":
            destroy_window(window)
        destroy_window(window)
    elif abs(int(user_input.get()) - 5) <= 3:
        CTkMessagebox(title="Close", message="how could you forget our first time?")
    else:
        CTkMessagebox(title="Wrong answer", message=bad_message_list[randint(0, len(bad_message_list) - 1)])


# first qn
window = new_window("Q3", '600x150')

l1 = CTkLabel(window, text="How many cuts on my wrist did we do on our first time?")
user_input = StringVar()
textbox = CTkEntry(window, textvariable=user_input)
b1 = CTkButton(window, command=check_q1, text="I'm confident")  # Remove parentheses
l1.grid(row=0, column=0)
textbox.grid(row=1, column=0)
b1.grid(row=3, column=0)

window.mainloop()