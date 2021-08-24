from turtle import Screen, distance
import turtle
from snake import Snake
from food import Food
from scoreboard import Score
import time

# positions = [(0,0), (-20,0), (-40,0)]
# segments = []
score = 0

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect the collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Detect crossing the boundary
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # score.gameover()
        # game_on = False
        score.reset()
        snake.reset()

    # Detect the tail collision
    for segment in snake.segments[1:]:
        # if segment == snake.head:
        #     pass
        # if snake.head.distance(segment) < 10:
        #     game_on = False
        #     score.gameover()
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()
        

screen.exitonclick()

