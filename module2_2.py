from tkinter.simpledialog import Dialog
from tkinter import Tk, Label, Frame, Button, LEFT

WIN_TITLE = "Module 2(2)"
LABEL_TEXT = "Ще який-небудь текст"
BACK_TEXT = "< Назад"
OK_TEXT = "Так"
CANCEL_TEXT = "Відміна"

class Dialog22(Dialog):
    result = None
    
    def __init__(self, window):
        title = WIN_TITLE
        Dialog.__init__(self, window, title)
    
    def body(self, window):
        Label(window, text = LABEL_TEXT).pack()
      
    def buttonbox(self):
        box = Frame(self)
        Button(box, text = BACK_TEXT, command = self.back).pack(side = LEFT)
        Button(box, text = OK_TEXT, command = self.ok).pack(side = LEFT)
        Button(box, text = CANCEL_TEXT, command = self.cancel).pack(side = LEFT)
        box.pack()

    def back(self):
        self.apply(True)
        self.cancel()

    def apply(self, back = False):
        self.result = -1 if back else 1


