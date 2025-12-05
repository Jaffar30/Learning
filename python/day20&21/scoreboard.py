from turtle import Turtle

class ScoreBoard(Turtle):   
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.update()
        self.hideturtle()

    def update(self):
        self.write(f"Score: {self.score}" , align="center" , font=("Arial" , 24 , "normal"))

    def increse_score(self):
        self.score +=1
        self.clear()
        self.update()