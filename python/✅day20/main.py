from turtle import Screen
import time
from snake import Snake
from food import Food

# I skipped the rest of the logic easy and already did it before

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

# stop auto animation and do it manually
screen.tracer(0) # turn off auto animation

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
    

screen.exitonclick()



# python slicing
# work for list and tuple

# 0 1 2 3 4 5 6
# a b c d e f g
#    [_____]
# from 2 till 5 : include 2 and when reach 5 stop and dont include 5
# piano_keys[2:5]
# ourput = c,d,e

# piano_keys[:5]
# a,b,c,d,e

# piano_keys[2:5:2]
# c,e

# piano_keys[::2]
# a,c,e,g

# piano_keys[::-1]
# reverse the list
# g,f,e,d,c,b,a