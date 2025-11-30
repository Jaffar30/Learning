from quiz import Quiz


def main():
    print("Welcome to the project!")
    quiz_title = input("Enter the title of the quiz: ")
    quiz = Quiz(quiz_title)
    quiz.prepare_quiz()
    quiz.take_quiz()

main()