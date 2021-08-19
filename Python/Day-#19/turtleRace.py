from turtle import Turtle, Screen
import random
import turtle

colors = ['red', "orange", "yellow", "green", "blue", "purple"]
y_position = [-50, -30, -10, 10, 30, 50]
turtles = []

def start_race(turtle_count:int):
    for n in range(turtle_count):
        turtle_color = colors[n]
        turtle_name = Turtle(shape="turtle")
        turtle_name.color(turtle_color)
        turtle_name.penup()
        # turtle_postition = int(230 / turtle_count) * n
        turtle_name.setposition(x=-230, y=y_position[n])
        turtles.append(turtle_name)


screen = Screen()
screen.setup(width=500, height=400)
choosen_player = screen.textinput("Turtle Race - Make your bet", "Who will win the race? Enter a colour:").lower()

if choosen_player:
    is_race_on = True

start_race(6)
while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == choosen_player:
                print(f"You've won! the {winning_color} turtle is the winner!")
            else:
                
                print(f"You've lost! the {winning_color} turtle is the winner!")
        distance = random.randint(1, 10)
        turtle.forward(distance)

screen.exitonclick()