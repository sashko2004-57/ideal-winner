from module1 import Dialog1
from module2_1 import Dialog21
from module2_2 import Dialog22
from tkinter import Tk, Label, Button, DISABLED

WIN_TITLE = "Головне вікно"
WIN_SIZE = "600x600"
BUTTON1_NAME = "Робота 1"
BUTTON2_NAME = "Робота 2"
LEFT_MOUSE_BUTTON_PRESS = "<1>"
TEXT_OPT = "text"

def open_dialog1(label, window):
    dialog = Dialog1(window)
    label[TEXT_OPT] = dialog.result
    #window.update()

def open_dialog2_1(window):
    while True:
        dialog = Dialog21(window)
        if dialog.result:
            result = open_dialog2_2(window)
            if not result:
                return
        else:
            return
    

def open_dialog2_2(window):
    dialog = Dialog22(window)
    if dialog.result == -1:
        return -1
    else:
        return

def main():
    result = ""
    window = Tk()
    window.title(WIN_TITLE)
    window.geometry(WIN_SIZE)
    label = Label(window, state = DISABLED)
    label.pack()
    button1 = Button(window, text = BUTTON1_NAME)
    button2 = Button(window, text = BUTTON2_NAME)
    button1.pack()
    button2.pack()
    button1.bind(LEFT_MOUSE_BUTTON_PRESS, lambda event : open_dialog1(label, window))
    button2.bind(LEFT_MOUSE_BUTTON_PRESS, lambda event : open_dialog2_1(window))

main()
