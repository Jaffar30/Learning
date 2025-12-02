# turtle graphics and tuples and import modules

from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
screen = Screen()

# TK color specification stringa ?
# what is TK : TK interface(tkinter) is a library for creating graphical user interfaces - GUI


# code
timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
timmy_the_turtle.color((random.randint(0, 255)/255, random.randint(0, 255)/255, random.randint(0, 255)/255))

timmy_the_turtle.right(90)
timmy_the_turtle.forward(100)
# code















# must be last line cause its block the thread until clicked
screen.exitonclick()
