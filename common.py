from CTkMessagebox import CTkMessagebox
from customtkinter import *
from random import randint
from time import sleep
from PIL import Image
from tkinter import *
import subprocess
import sys


# wrong answer array
bad_message_list = ["Dumbassery incarnate",
                    "Hope you 96.9 all your 14+ses",
                    "trincakes common L",
                    "i hope your heels break again",
                    "cursing you to scuff all your handbags on first use",
                    "i hope your reds never match",
                    "our wrenally",
                    "my favourite girlfailure",
                    "im gonna block you if you get it wrong again",
                    "i hope the lace on your dress get frayed",
                    "bad girls should get punished",
                    "no more midnight boba for you"]


# functions
def new_window(title, window_size="600x150"):
    """ Creates a new window object with title as the window title
        and window_size as the window size parameter"""
    window = CTk()
    window.title(title)
    window.geometry(window_size)
    set_appearance_mode("dark")
    window.protocol('WM_DELETE_WINDOW', end_program)

    return window


def destroy_window(window):
    """destroys the window provided in argument"""
    window.destroy()


def end_program():
    """terminates the entire python program"""
    sys.exit()


def call_next_script(script_path):
    """ spaghetti code to get the entire program to run correctly because customtkinter has issues constructing multiple
        windows for some godforsaken reason"""
    subprocess.run([sys.executable, '-m', 'venv/Scripts/activate_this.py'])
    result = subprocess.run([sys.executable, script_path], capture_output=True, text=True)
    return result
