#!/usr/bin/env python
from tkinter import *
from question import Question

class Application(Frame):
    def __init__(self, master=Tk()):
        Frame.__init__(self, master)
        master.title('Quizma')
        master.geometry('300x200')
        self.pack()
        self.load_quiz('example.md')
        self.create_widgets()
    
    def create_widgets(self):
        self.question_label_text = StringVar()
        self.question_label_text.set(self.questions[-1].text)

        self.question_label = Label(self, textvariable=self.question_label_text)
        self.question_label.pack()

        self.proceed_button_text = StringVar()
        self.proceed_button_text.set('Next')

        self.proceed_button = Button(self, textvariable=self.proceed_button_text)
        self.proceed_button.pack()
    
    def load_quiz(self, filename):
        self.quiz_title = ''
        self.questions = []
        with open(filename, 'r') as f:
            for line in f:
                if line.startswith('##'):
                    q = Question(line.replace('##', ''))
                    self.questions.append(q)
                    continue
                elif line.startswith('-'):
                    q = self.questions[-1]
                    q.answers.append(line.replace('-', ''))
                    continue
                elif line.startswith('#'):
                    self.quiz_title = line.replace('#', '')


app = Application()
app.mainloop()