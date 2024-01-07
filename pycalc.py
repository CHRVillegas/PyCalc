from tkinter import *

#Frame creation for calculator
def iCalc(source, side):
    storeObj = Frame(source, borderwidth = 4, bd = 4, bg = "powder blue")
    storeObj.pack(side = side, expand = YES, fill = BOTH)
    return storeObj

#Generating Button
def button(source, side, text, command = NONE):
    storeObj = Button(source , text = text, command = command)
    storeObj.pack(side = side, expand = YES, fill = BOTH)
    return storeObj

class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'arial 20 bold')
        self.pack(expand = YES, fill = BOTH)
        self.master.title('Calculator')
        display = StringVar()
        Entry(self, relief = RIDGE, textvariable = display, justify = 'right', bd = 30, bg = "powder blue").pack(side = TOP, expand = YES, fill = BOTH)

#GUI Generation
if __name__ == '__main__':
    app().mainloop()