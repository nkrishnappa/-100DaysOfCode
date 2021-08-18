from turtle import Turtle, Screen, degrees, distance
import random
import turtle

t = Turtle()
screen = Screen()
t.shape("turtle")
t.color("orange")
colors = ["blue", "BlueViolet", "brown", "chartreuse", "chocolate", "cyan", "DarkBlue", "DarkOrchid", "coral"]

'''
# Draw Square - 100 spaces
for _ in range(4):
    t.forward(100)
    t.left(90)
'''

'''
# Draw Dashed Line
for _ in range(20):
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()
'''

'''
# Draw Triangle, square, ....
def draw(sides):
    degree = 360 / sides
    for _ in range(sides):
        t.forward(100)
        t.right(degree)

for n in range(3,10):
    draw(n)
    t.color(random.choice(colors))
'''

'''
# Random Walk
direction = [0, 90, 180, 270]
t.pensize(10)
t.speed('fast')
for _ in range(200):
    distance = random.randint(20,50)
    t.color(random.choice(colors))
    t.setheading(random.choice(direction))
    t.forward(distance)
'''

'''
# Random Walk with RGB
turtle.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)

direction = [0, 90, 180, 270]
t.pensize(10)
t.speed('fast')
for _ in range(200):
    distance = random.randint(20,50)
    t.color(random_color())
    t.setheading(random.choice(direction))
    t.forward(distance)
'''

'''
# make a spirograph
turtle.colormode(255)
t.speed('fastest')

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        t.color(random_color())
        t.circle(100)
        t.setheading(t.heading() + size_of_gap)
draw_spirograph(5)

# # make a spirograph
# for _ in range(50):
#     t.color(random_color())
#     t.circle(100)
#     t.left(10)
'''

screen.exitonclick()