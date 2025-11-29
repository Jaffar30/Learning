# OOP
# using Turtle module
# pascal case naming convention for class names : FirstLetterOfEachWordIsCapitalized
# import turtle
from turtle import Turtle,Screen
from prettytable import PrettyTable

# timmy = Turtle()
# my_screen = Screen()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
# print(my_screen.canvheight)
# print(my_screen['canvheight'])  cant use this way
# exit after I click on the screen
# my_screen.exitonclick()

# ====================================
table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
print(table)