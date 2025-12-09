from turtle import Turtle
START = [(0,0) , (-20,0),(-40,0)]
MOVE = 20   
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.parts = []
        self.create_snake()
        self.head = self.parts[0]
    
    def create_snake(self):
        for loc in START:
            self.add_part(loc)

    def add_part(self , loc):
        new_part = Turtle("square")
        new_part.color("white")
        new_part.penup()
        new_part.goto(loc)  
        self.parts.append(new_part)

    def extend(self):
        self.add_part(self.parts[-1].position())
    
    def move(self):
        for i in range(len(self.parts) -1 , 0 , -1):
            new_x = self.parts[i - 1].xcor()
            new_y = self.parts[i - 1].ycor()
            self.parts[i].goto(new_x,new_y)
        self.head.forward(MOVE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
                self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:    
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def compute_game_over(self):
        if abs(self.head.xcor()) > 270 or abs(self.head.ycor()) > 270:
            self.head.goto(0,0)
            self.head.write("Game Over", align="center" , font=('Arial', 30, 'normal'))
            return True
        for part in self.parts[1:]:
            if self.head.distance(part) < 10:
                self.head.write("Game Over", align="center" , font=('Arial', 30, 'normal'))
                return True