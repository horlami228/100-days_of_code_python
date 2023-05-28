from turtle import *
import turtle
import pandas

screen = Screen()
image = "US_image.gif"
screen.addshape(image)
screen.title("U.S States Game")
turtle.shape(image)

data = pandas.read_csv("US-states.csv")
all_us_states = data.state.to_list()

total_states = 50
guessed_state = []

while len(guessed_state) < 50:
    answer_text = turtle.textinput(title=f"{len(guessed_state)}/{total_states} States Correct",
                                   prompt="What's another state name?").title()
    if answer_text == "Exit":
        missing_state = {"State": []}
        for state in all_us_states:
            if state not in guessed_state:
                missing_state["State"].append(state)

        data = pandas.DataFrame(missing_state)
        data.to_csv("missing_state.csv")
        break

    if answer_text in all_us_states:
        selected = data[data.state == answer_text]
        guessed_state.append(answer_text)
        x_cor = selected.x
        y_cor = selected.y

        st = Turtle()
        st.penup()
        st.hideturtle()

        st.goto(int(x_cor), int(y_cor))
        st.write(answer_text, font=('Arial', 7, 'normal'))

