from tkinter as tk

def iCalc(source, side):
    storeObj = Frame(source, borderwidth = 1, bd=4, bg="powder blue")
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj

def button(source, side, text, command=None):
    storeObj = Button(source, text=text, command=command)
    storeObj.pack(side=side, expand=Yes, fill=BOTH)
    return storeObj

class app(Frame):
    def _init_(self):
        Frame._init_(self)
        self.option_add('*Front','arial 20 bold')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Calculator')

if _name_=='_main_':
    app().mainloop()
