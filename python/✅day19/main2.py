from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make Your Bet",prompt="Which turtle will win the race? Enter a color: ")

tim.goto(x=-250,y=0)




screen.exitonclick()

# skip the rest already know and did before easy