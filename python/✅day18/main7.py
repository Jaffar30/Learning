# my way
# # draw a dashed line
# from turtle import Turtle, Screen
# from random import randint

# def main():
#     screen = Screen()
#     turtle = Turtle()
#     turtle.speed("fastest")

#     for i in range(100):
#         turtle.color((randint(0, 255)/255, randint(0, 255)/255, randint(0, 255)/255))
#         turtle.circle(100)
#         turtle.right(10)

    
    
    
#     screen.exitonclick()

# main()


# draw a dashed line

# second way
from turtle import Turtle, Screen
from random import randint

def main():
    screen = Screen()
    turtle = Turtle()
    turtle.speed("fastest")
    

    for i in range(100):
        turtle.color((randint(0, 255)/255, randint(0, 255)/255, randint(0, 255)/255))
        turtle.circle(100)
        turtle.setheading(turtle.heading()+10)

    
    
    
    screen.exitonclick()

main()