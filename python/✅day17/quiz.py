from question import Question

class Quiz:
    QUIZ_ID = 0

    def __init__(self, title):
        Quiz.QUIZ_ID += 1
        self.id = Quiz.QUIZ_ID
        self.title = title
        self.score = 0
        self.total_score = 0
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)
        self.total_score += 1

    def prepare_quiz(self):
        print(f"Quiz: {self.title} (ID: {self.id})")
        while True:
            question_text = input("Enter question (or 'done' to finish): ")
            if question_text.lower() == 'done':
                break
            answer_text = input("The question answer is True or False ?").lower()
            while answer_text not in ['true', 'false']:
                print("Please enter 'True' or 'False'.")
                answer_text = input("The question answer is True or False ?").lower()
            
            question = Question(question_text,answer_text)
            self.add_question(question)

    def take_quiz(self):
        print(f"Starting Quiz: {self.title}")
        for question in self.questions:
            user_answer = input(f"{question.name} (True/False): ").lower()
            while user_answer not in ['true', 'false']:
                print("Please enter 'True' or 'False'.")
                user_answer = input(f"{question.name} (True/False): ").lower()
            

            if question.check_answer(user_answer= user_answer):
                print("Correct!")
                self.score += 1
            
            print(f"Score: {self.score}/{self.total_score}")
            