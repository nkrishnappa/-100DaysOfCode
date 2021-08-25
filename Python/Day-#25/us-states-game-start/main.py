from turtle import Turtle, Screen
import turtle
import pandas


state_csv_file = r"C:\Users\nkrishnappa\Desktop\100DaysOfCode\Python\Day-#25\us-states-game-start\50_states.csv"
image = r"C:\Users\nkrishnappa\Desktop\100DaysOfCode\Python\Day-#25\us-states-game-start\blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S States Game")
# screen.bgpic(image)

screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv(state_csv_file)

guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states guessed correctly", prompt="What's another state's name?").lower()
    # Nandisha Solution
    if answer_state == "exit":
        break

    if data[data["state"].str.lower() == answer_state].shape[0]:
        state_info = data[data["state"].str.lower() == answer_state].values[0]
        # ['Massachusetts' 312 112]
        states = Turtle()
        states.hideturtle()
        states.penup()
        states.color("black")
        states.goto(state_info[1], state_info[2])
        states.write(f"{state_info[0]}", align="center", font=("Arial", 6, "normal"))
        if state_info[0] not in guessed_states:
            guessed_states.append(state_info[0])

missing_state = []
for state in data.state:
    if state not in guessed_states:
        missing_state.append(state)
new_data = pandas.DataFrame(missing_state)
new_data.to_csv(r"C:\Users\nkrishnappa\Desktop\100DaysOfCode\Python\Day-#25\us-states-game-start\states_missed_guess.csv")

# screen.exitonclick()
"""
# what is the position 

def get_mouse_click_coor(x, y):
    print(x,y)
turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()

screen.exitonclick()

"""
