from turtle import Turtle

class ScoreBoard(Turtle):   
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("python\day24\snack\data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.update()
        self.hideturtle()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}" , align="center" , font=("Arial" , 24 , "normal"))
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("python\day24\snack\data.txt" , mode="w") as data:
                data.write(f"{self.high_score}")

        self.score = 0 
        self.update()

    def increse_score(self):
        self.score +=1
        self.clear()
        self.update()