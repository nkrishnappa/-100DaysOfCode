'''
import colorgram

# Extract 6 colors from an image.
colors = colorgram.extract('image.jpg', 10)

# for color in colors:
#     print(f"{color}")

colors_list = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)

    colors_list.append(new_color)

print(colors_list)

'''

from turtle import Screen, Turtle
import random
import turtle
colors_list = [ (236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216), (52, 93, 124), (172, 154, 48)]

t = Turtle()
screen = Screen()

t.penup()
t.setposition(-300, -300)

t.speed('fast')
turtle.colormode(255)

dot_count = 10
dot_size = 20
forward_size = 50

def draw_hirizon(dots):
    for _ in range(dots + 1):
        t.dot(dot_size, random.choice(colors_list))
        t.forward(forward_size)

def retrace(dots):
    t.right(180)
    t.forward(forward_size * (dots + 1))
    t.right(90)
    t.forward(forward_size)
    t.right(90)

for _ in range(dot_count):
    draw_hirizon(dot_count)
    retrace(dot_count)

t.hideturtle()
screen.exitonclick()