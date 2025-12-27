from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.tracer(0)
snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(snake.up , "Up")
screen.onkey(snake.down , "Down")
screen.onkey(snake.right , "Right")
screen.onkey(snake.left , "Left")

game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.compute_game_over():
        score_board.reset()
        game_on = False
    if snake.head.distance(food) < 15:
        food.update_loc() 
        snake.extend()
        score_board.increse_score()

screen.exitonclick()