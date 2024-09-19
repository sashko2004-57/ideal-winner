from tkinter.simpledialog import Dialog
from tkinter import Label, Scale, Frame, Button, HORIZONTAL, LEFT

WIN_TITLE = "Module 1"
LABEL_TEXT = "Обери ціле число від 1 до 100:"
OK_TEXT = "Так"
CANCEL_TEXT = "Відміна"
MAX_NUM = 100
SCALE_LEN = 300

class Dialog1(Dialog):
    result = None
    
    def __init__(self, window):
        title = WIN_TITLE
        Dialog.__init__(self, window, title)

    def body(self, window):
        Label(window, text = LABEL_TEXT).pack()
        self.__scale = Scale(window, from_ = 1, to = MAX_NUM, length = SCALE_LEN, orient=HORIZONTAL)
        self.__scale.pack()

    def buttonbox(self):
        box = Frame(self)
        Button(box, text=OK_TEXT, command=self.ok).pack(side=LEFT)
        Button(box, text=CANCEL_TEXT, command=self.cancel).pack(side=LEFT)
        box.pack()

    def apply(self):
        self.result = self.__scale.get()
