from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.restart()
    
    def move(self):
        self.forward(MOVE_DISTANCE)

    def restart(self):
        self.setposition(STARTING_POSITION)
    
    def player_at_finish_line(self):
        return self.ycor() > 280 