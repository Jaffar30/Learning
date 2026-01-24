from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self , quiz_question: QuizBrain):
        self.quiz = quiz_question
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(padx=20,pady=20, bg=THEME_COLOR)

        self.score_text = Label(text="Score : 0",fg="white" , bg=THEME_COLOR)
        self.score_text.grid(row=0,column=1)

        self.canvas = Canvas(width=300,height=250,bg="white")
        self.question = self.canvas.create_text(150,125,width=280,text="Question", fill=THEME_COLOR , font=("Arial" , 20,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=2 , pady=50)

        self.right_img = PhotoImage(file="images/true.png")
        self.correct_button = Button(image=self.right_img,highlightthickness=0,command=self.true_click)
        self.correct_button.grid(row=2,column=1)

        self.wrong_img = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=self.wrong_img,highlightthickness=0,command=self.false_click)
        self.wrong_button.grid(row=2,column=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_text.config(text=f"Score : {self.quiz.score}")
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.question,text=question)
        else:
            self.canvas.itemconfig(self.question , text="The Quiz is end")
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_click(self):
        self.answor_checker(self.quiz.check_answer("True"))

    def false_click(self):
        self.answor_checker(self.quiz.check_answer("False"))

    def answor_checker(self,is_right:bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)