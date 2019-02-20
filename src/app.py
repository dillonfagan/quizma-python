#!/usr/bin/env python
from tkinter import *

class Application(Frame):
    def __init__(self, master=Tk()):
        Frame.__init__(self, master)
        master.title('Quizma')
        master.geometry('300x200')
        self.pack()
        self.create_widgets()
    
    def create_widgets(self):
        self.question_label_text = StringVar()
        self.question_label_text.set('Is this a question?')

        self.question_label = Label(self, textvariable=self.question_label_text)
        self.question_label.pack()

        self.proceed_button_text = StringVar()
        self.proceed_button_text.set('Next')

        self.proceed_button = Button(self, textvariable=self.proceed_button_text)
        self.proceed_button.pack()


app = Application()
app.mainloop()