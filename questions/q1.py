from common import *


def check_q1():
    if user_input.get().lower() == "fixer":
        msg = CTkMessagebox(title="Not bad not bad", message="Good job, moving on", option_1="Yay")
        response = msg.get()
        if response == "Yay":
            destroy_window(window)
        destroy_window(window)
    elif user_input.get().lower() == "solips":
        CTkMessagebox(title="Vain much?", message="close, but that's my favourite PERSON, not my favourite song")
    elif user_input.get().lower() == "decadism":
        CTkMessagebox(title="Vain much?", message="YOU'RE the one who said not to appropriate your favourite song smh")
    elif user_input.get().lower() in ["just life", "empty prayer", "haze", "fragile", "aoku aoku hikaru", "outer sample"
                                      ,"lower one's eyes", "folern"]:
        CTkMessagebox(title="Nulut FTW", message="Good guess from my favourite Nulut fangirl but unfortunately you're "
                                                 "wrong")
    elif user_input.get().lower() in ["enchanted", "i'm glad you're evil too", "android girl"]:
        CTkMessagebox(title="Almost correct", message="surprised you guessed this but you already know the correct "
                                                      "answer LMAO")
    else:
        CTkMessagebox(title="Wrong answer", message=bad_message_list[randint(0, len(bad_message_list) - 1)])


# first qn
window = new_window("Q1", '600x150')

l1 = CTkLabel(window, text="What's Sean's favourite song?")
user_input = StringVar()
textbox = CTkEntry(window, textvariable=user_input)
b1 = CTkButton(window, command=check_q1, text="I'm confident")  # Remove parentheses
l1.grid(row=0, column=0)
textbox.grid(row=1, column=0)
b1.grid(row=2, column=0)

window.mainloop()
