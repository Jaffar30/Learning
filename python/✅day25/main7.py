# turtle only work with .gif images
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_states = []
data = pandas.read_csv("50_states.csv")

# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

while len(guessed_states) < 50:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")

    if answer_state == "Exit":
        break

    if answer_state in data["state"].to_list() and not answer_state in guessed_states:
        guessed_states.append(answer_state)

        state_data = data[data.state == answer_state]

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        t.write(answer_state, align="center", font=("Arial", 8, "normal"))
screen.exitonclick()
# turtle.mainloop() # keep the window open until user closes it even on clicking the turtle window