
class Question:
    def __init__(self, text='', answers=[], correct_answer_index=0):
        self.text = text
        self.answers = answers
        self.correct_answer_index = correct_answer_index
    
    def get_correct_answer(self):
        return self.answers[self.correct_answer_index]
    
    correct_answer = property(get_correct_answer)