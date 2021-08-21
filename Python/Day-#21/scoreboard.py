from turtle import Turtle

class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.game_score = 0
        self.penup()
        self.color("white")
        self.setpos(0,270)
        self.hideturtle()
        self.update_score()
        self.write(f"Score : {self.game_score}", move=False, align="center", font=("Lemon", 20, "normal"))
        
    def update_score(self):
        self.clear()
        self.game_score += 1 
        self.write(f"Score : {self.game_score}", move=False, align="center", font=("Lemon", 20, "normal"))
    
    def gameover(self):
        self.setpos(0,0)
        self.write("GAME OVER", align="center", font=("Lemon", 20, "normal"))