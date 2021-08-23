from turtle import Turtle, left
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setposition(-270,250)
        self.player_score = 0
        self.penup()
        self.color("Black")
        self.write(self.player_score, align="left", font=FONT)
        
    def update_score(self):
        self.player_score += 1
        self.clear()
        self.write(self.player_score, align="left", font=FONT)
