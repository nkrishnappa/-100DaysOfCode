from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_position, y_position) -> None:
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.width(20)
        self.x_position = x_position
        self.y_position = y_position
        self.setposition(self.x_position, self.y_position)

    def moveup(self):
        new_y = self.ycor() + 20
        self.setposition(self.xcor(), new_y)

    def movedown(self):
        new_y = self.ycor() - 20
        self.setposition(self.xcor(), new_y)