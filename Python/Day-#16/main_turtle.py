from turtle import Turtle, Screen
import turtle

# object = Class
timmy = Turtle()
print(timmy) # <turtle.Turtle object at 0x002FF700>

my_screen = Screen()
# Attributes
print(my_screen.canvheight, my_screen.canvwidth)

# Functions tied with class/object we call methods
turtle.shape("turtle")
turtle.color("DarkOrange")

turtle.forward(100)
my_screen.exitonclick()
