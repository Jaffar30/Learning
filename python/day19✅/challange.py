from turtle import Turtle, Screen

turtle = Turtle()

def forward():
    turtle.forward(10)
def backward():
    turtle.backward(10)
def turn_left():
    turtle.left(10)
def turn_right():
    turtle.right(10)


screen = Screen()
screen.listen()
screen.onkey(forward, "w")
screen.onkey(backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(screen.clearscreen, "c")
screen.exitonclick()