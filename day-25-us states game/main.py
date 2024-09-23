from turtle import Turtle, Screen
import pandas

turtle = Turtle()
screen = Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")

game_is_on = True
correct_guess = []
list_of_states = data.state.to_list()


while len(correct_guess) < 50:

    answer_state = screen.textinput(title=f"{len(correct_guess)}/50 States Correct", prompt="What's another state's name?").title()


    if answer_state == "Exit":
        learn_state = [state for state in list_of_states if state not in correct_guess]
        learning_data = pandas.DataFrame(learn_state)
        learning_data.to_csv("states_to_learn.csv")
        break

    if answer_state in list_of_states:
        if answer_state in correct_guess:
            print("You've already guessed this state. try again")

        else:
            t = Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer_state]
            t.goto(int(state_data.x), int(state_data.y))
            t.write(answer_state)
            correct_guess.append(answer_state)



