from turtle  import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
POSITIONS = [-240, -210, -180, -150, -120, -90, -60, -30, 0, 30, 60, 90, 120, 150, 180, 210, 240]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.cars_list = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance != 1:
            return
        new_car = Turtle()
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.shape("square")
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        # new_car.setheading(180)
        x_axis = 300
        y_axis = random.choice(POSITIONS)
        new_car.setposition(x_axis, y_axis)
        self.cars_list.append(new_car)      
        
    def move_car(self):
        for car in self.cars_list:
            car.backward(self.car_speed)

    def increase_level(self):
        self.car_speed += MOVE_INCREMENT
