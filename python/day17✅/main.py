from data import question_data
from question import Question
from quiz_structure import QuizStructure

question_storage = []
for rec in question_data["results"]:
    question_storage.append(Question(rec["question"], rec["correct_answer"]))

quiz = QuizStructure(question_storage)
while quiz.question_number < len(quiz.question_list):
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{len(question_storage)}")
