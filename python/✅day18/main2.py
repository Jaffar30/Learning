from turtle import Turtle, Screen

# draw square

def draw_square(turtle,square_length):
    for i in range(4):
        turtle.forward(square_length)
        turtle.right(90)

def main():
    screen = Screen()
    turtle = Turtle()
    draw_square(turtle, 100)
    screen.exitonclick()

main()