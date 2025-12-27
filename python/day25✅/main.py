import turtle
import pandas

screen = turtle.Screen()
map_image = "blank_states_img.gif"
screen.addshape(map_image)
turtle.shape(map_image)
data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
correct_guess = []
while len(correct_guess) < len(states):
    user_input = turtle.textinput(f"You got {len(correct_guess)} out of {len(states)}","guess").title()
    
    if user_input in ['Exit' , 'E']:
        miss = []
        for state in states:
            if state not in correct_guess:
                miss.append(state)
        pandas.DataFrame(miss).to_csv("missing_state")
        break
    if user_input in states and not user_input in correct_guess:
        print(data['state'] == user_input)
        loc = data[data['state'] == user_input]
        # print(loc)
        typer = turtle.Turtle()
        typer.hideturtle()
        typer.penup()
        typer.goto(loc['x'].item(), loc['y'].item())
        typer.write(loc['state'].item())
        correct_guess.append(user_input)
        print(correct_guess)