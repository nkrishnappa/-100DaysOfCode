from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.right_scores = 0
        self.left_scores = 0
        self.hideturtle()
        self.display_score()
        
    def right_scored(self):
        self.right_scores += 1
        self.display_score()
        
    def left_scored(self):
        self.left_scores += 1
        self.display_score()

    def display_score(self):
        self.clear()
        self.goto(-100,240)
        self.write(self.left_scores, align="center", font=("Courier", 40, "normal"))        
        self.goto(100,240)
        self.write(self.right_scores, align="center", font=("Courier", 40, "normal"))

