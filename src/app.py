#!/usr/bin/env python
from tkinter import *

class Application(Frame):
    def __init__(self, master=Tk()):
        Frame.__init__(self, master)
        master.title('Quizma')
        master.geometry('300x200')
        self.pack()


app = Application()
app.mainloop()