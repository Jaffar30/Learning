# draw a dashed line
from turtle import Turtle, Screen
from random import choice,randint

DIRECTIONS = [0,90,180,270]

def main():
    screen = Screen()
    turtle = Turtle()
    turtle.pensize(15)
    turtle.speed("fastest")
    turtle.shape("square")

    for i in range(100):
        turtle.color((randint(0, 255)/255, randint(0, 255)/255, randint(0, 255)/255))
        turtle.forward(100)
        turtle.right(choice(DIRECTIONS))
    
    screen.exitonclick()

main()