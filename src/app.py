#!/usr/bin/env python
from tkinter import *
from tkinter import filedialog
from question import Question

class Application(Frame):
    def __init__(self, master=Tk()):
        Frame.__init__(self, master)
        master.title('Quizma')
        master.geometry('500x300')
        self.pack()
        self.show_welcome_frame()
    
    def show_welcome_frame(self):
        self.open_file_label = Label(self, text='Open a quiz file.').pack()
        self.open_button = Button(self, text='Choose file', command=self.open_quiz_file).pack()
    
    def show_quiz_frame(self):
        for w in self.pack_slaves():
            w.destroy()

        self.question_label_text = StringVar()
        self.question_label_text.set(self.questions[-1].text)

        self.question_label = Label(self, textvariable=self.question_label_text).pack()

        self.proceed_button_text = StringVar()
        self.proceed_button_text.set('Next')

        self.proceed_button = Button(self, textvariable=self.proceed_button_text).pack()

    def open_quiz_file(self):
        filename = filedialog.askopenfilename(initialdir='/', title='Choose file', filetypes=(("markdown files","*.md"),("all files","*.*")))
        self.load_quiz(filename)
        self.show_quiz_frame()
    
    def load_quiz(self, filename):
        self.quiz_title = ''
        self.questions = []
        with open(filename, 'r') as f:
            for line in f:
                if line.startswith('##'):
                    q = Question(line.replace('##', ''))
                    self.questions.append(q)
                elif line.startswith('-'):
                    q = self.questions[-1]
                    if line.startswith('- A:'):
                        q.answers.append(line.replace('- A:', ''))
                        q.correct_answer_index = len(q.answers) - 1
                    else:
                        q.answers.append(line.replace('-', ''))
                elif line.startswith('#'):
                    self.quiz_title = line.replace('#', '')


app = Application()
app.mainloop()