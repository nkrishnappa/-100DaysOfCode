"""
 - Main 
    - screen
 - ScoreCard - 2 cards 
    - class ScoreCard(Turtle)
 - 2 Paddle
    - class Paddle(Turtle)
 - Ball
    - class Ball(Turtle)
    - Detect collision with wall and bounce
    - Detect collision with Peddle
"""
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.title("The Pong Game")
screen.setup(width=800, height=600)
screen.tracer(0)

right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
ball = Ball()
score = ScoreBoard()

screen.listen()
screen.onkey(right_paddle.moveup, "Up")
screen.onkey(right_paddle.movedown, "Down")
screen.onkey(left_paddle.moveup, "w")
screen.onkey(left_paddle.movedown, "s")

game_on = True
while game_on == True:
    screen.update()
    time.sleep(ball.moving_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    # ball misses right
    if ball.xcor() > 350:
        score.left_scored()
        ball.reset_position()

    # ball misses left 
    if ball.xcor() < -350:
        score.right_scored()
        ball.reset_position()
        # ball = Ball()

screen.exitonclick()