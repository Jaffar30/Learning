# draw a dashed line
from turtle import Turtle, Screen
from random import randint


def main():
    screen = Screen()
    turtle = Turtle()

    for i in range(3, 11):
        turtle.color((randint(0, 255)/255, randint(0, 255)/255, randint(0, 255)/255))
        for j in range(i):
            turtle.forward(100)
            turtle.right(360/(i))
    
    
        
        

    screen.exitonclick()

main()