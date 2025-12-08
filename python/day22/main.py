from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)
right = Paddle((350 , 0))
left = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right.go_up, "Up")
screen.onkey(right.go_down, "Down")
screen.onkey(left.go_up, "w")
screen.onkey(left.go_down, "s")


game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    if ball.ycor() > 200 or ball.ycor() < 200:
        ball.bounce_y()
    if ball.distance(right) < 50 and ball.xcor() > 320 or ball.distance(left) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    if ball.xcor() > 380:
        ball.reset_raound()
        scoreboard.right_point()
    if ball.xcor() < -380:
        ball.reset_raound()
        scoreboard.left_point()

screen.exitonclick()