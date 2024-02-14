from common import *
from ctypes import windll, byref, sizeof, c_int


def create_windows():
    heart_coords = ['885+300',
                    '750+275', '700+250', '650+275', '600+300', '650+400', '700+500', '800+600',            # left side
                    '1020+275', '1070+250', '1120+275', '1170+300', '1120+400', '1070+500', '970+600',      # right side
                    '885+675']
    window.geometry("400x310+1500+770")
    # bg color
    new_window = CTkToplevel(window)
    new_window.title("<3")
    new_window.configure(fg_color='#ff4da6')
    new_window.geometry("400x310+760+340")

    HWND = windll.user32.GetParent(new_window.winfo_id())
    tb_color = 0x00a64dff
    windll.dwmapi.DwmSetWindowAttribute(
        HWND,
        35,
        byref(c_int(tb_color)),
        sizeof(c_int)
    )

    iconpath = PhotoImage(file="../resources/hotpink.png")
    new_window.wm_iconbitmap()
    new_window.after(300, lambda: new_window.iconphoto(False, iconpath))

    for i in heart_coords:
        new_window = CTkToplevel(window)
        new_window.title("<3")
        new_window.configure(fg_color='#fac0e5')
        new_window.geometry('150x150+' + i)

        HWND = windll.user32.GetParent(new_window.winfo_id())
        tb_color = 0x00e5c0fa
        windll.dwmapi.DwmSetWindowAttribute(
            HWND,
            35,
            byref(c_int(tb_color)),
            sizeof(c_int)
        )

        iconpath = PhotoImage(file="../resources/pink.png")
        new_window.wm_iconbitmap()
        new_window.after(300, lambda: new_window.iconphoto(False, iconpath))
        sleep(0.35)


window = Tk()
window['background']='red'
window.geometry("400x310+760+340")
b1 = Button(text="Click me for a surprise", command=create_windows)
b1.pack(padx=20, pady=20)
window.mainloop()
