class Question:
    QUESTION_ID = 0

    def __init__(self,name,answer):
        Question.QUESTION_ID += 1
        self.id = Question.QUESTION_ID
        self.name = name
        self.answer = answer

    def check_answer(self, user_answer):
        return self.answer == user_answer