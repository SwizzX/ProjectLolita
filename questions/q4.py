from common import *


def check_q4():
    if user_input.get().lower() == "synesthesia ghost" or user_input.get().lower() == "kyoukankaku obake":
        msg = CTkMessagebox(title="And so many more since", message="Synesthesia ghost, Decadism, Fixer, Inochi Bakkari"
                                                                    ", Villain Re:Master, Aunno beats and most recently"
                                                                    " Manimani",
                            option_1="Cheers to many more")
        response = msg.get()
        if response == "Cheers to many more":
            destroy_window(window)
        destroy_window(window)
    else:
        CTkMessagebox(title="Wrong answer", message=bad_message_list[randint(0, len(bad_message_list) - 1)])


# first qn
window = new_window("Q3", '600x150')

l1 = CTkLabel(window, text="What was the first ever song I AP'ed to impress you?")
user_input = StringVar()
textbox = CTkEntry(window, textvariable=user_input)
b1 = CTkButton(window, command=check_q4, text="I'm confident")  # Remove parentheses
l1.grid(row=0, column=0)
textbox.grid(row=1, column=0)
b1.grid(row=3, column=0)

window.mainloop()
