from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from turtle import Turtle, Screen
import time

screen = Screen()
screen.tracer(0)

screen.setup(width=600, height=600)
player = Player()
score = Scoreboard()
car_manager = CarManager()


screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on == True:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    # collision
    for car in car_manager.cars_list:
        if car.distance(player) < 20:
            game_is_on = False

    if player.player_at_finish_line():
        player.restart()
        car_manager.increase_level()
        score.update_score()

screen.exitonclick()