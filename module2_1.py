from tkinter.simpledialog import Dialog
from tkinter import Tk, Label, Frame, Button, LEFT

WIN_TITLE = "Module 2(1)"
LABEL_TEXT = "Який-небудь текст"
NEXT_TEXT = "Далі >"
CANCEL_TEXT = "Відміна"

class Dialog21(Dialog):
    result = None
    
    def __init__(self, window):
        title = WIN_TITLE
        Dialog.__init__(self, window, title)
    
    def body(self, window):
        Label(window, text = LABEL_TEXT).pack()
      
    def buttonbox(self):
        box = Frame(self)
        Button(box, text = NEXT_TEXT, command = self.ok).pack(side = LEFT)
        Button(box, text = CANCEL_TEXT, command = self.cancel).pack(side = LEFT)
        box.pack()

    def apply(self):
        self.result = True
