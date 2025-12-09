import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_mang = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.on_up , "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_mang.create_cars()
    car_mang.move_cars()

    for car in car_mang.all_car:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()
    
    if player.end_line():
        player.start_pos()
        car_mang.levelup()
        score.increase_level()
        