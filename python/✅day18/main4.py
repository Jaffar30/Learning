# draw a dashed line
from turtle import Turtle, Screen

def draw_dashed_line(turtle,full_move_distance):
    for index,value in enumerate(range(10, full_move_distance + 1, 10)):
        step = value / (index+1)
        turtle.forward(int(step/2))
        turtle.penup()
        turtle.forward(int(step/2))
        turtle.pendown()


def main():
    screen = Screen()
    turtle = Turtle()
    draw_dashed_line(turtle=turtle,full_move_distance=1000)
    screen.exitonclick()

main()