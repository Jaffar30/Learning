from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def angle_left():
    tim.setheading(tim.heading()+10)

def angle_right():
    tim.setheading(tim.heading()-10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="space",fun=move_forwards)
screen.onkey(key="Right",fun=angle_right)
screen.onkey(key="Left",fun=angle_left)
screen.onkey(key="c",fun=clear)

screen.exitonclick()