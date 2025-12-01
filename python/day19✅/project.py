from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500 , height=400)
user_input = screen.textinput(title="Type your turtle color" , prompt="What is your input: ")
turtle_color = ["red" , "blue" , "green" , "purple"]
turtle_list = []
for i in range(0 , 4):
    turtle = Turtle(shape="turtle")
    turtle.color(turtle_color[i])
    turtle.penup()
    turtle.goto(x=-250 , y= i * 30)
    turtle_list.append(turtle)

is_still_looping = True
while is_still_looping:
    for tur in turtle_list:
        if tur.xcor() > 230:
            tur.goto(0,0)
            if tur.pencolor() == user_input:
                tur.write("You win", move=False, align='center', font=('Arial',30, 'normal'))
            else:
                tur.write("Ypu lose", move=False, align='center', font=('Arial', 30, 'normal'))
            is_still_looping = False
            screen.exitonclick()
        tur.forward(random.randint(1,10))


