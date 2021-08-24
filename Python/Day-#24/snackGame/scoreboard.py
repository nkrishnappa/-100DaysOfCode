from turtle import Turtle, update
FILE = "score.txt"

class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.game_score = 0
        with open(FILE) as data:
            self.high_score = int(data.read())
        self.penup()
        self.color("white")
        self.setpos(0,270)
        self.hideturtle()
        self.update_score()
        # self.write(f"Score : {self.game_score}", move=False, align="center", font=("Lemon", 20, "normal"))
    
    def write_highscore(self):
        with open(FILE, "w") as file:
            file.write(str(self.high_score))

    def increase_score(self):
        self.game_score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.game_score} High Score: {self.high_score}", move=False, align="center", font=("Lemon", 20, "normal"))
    
    # def gameover(self):
    #     self.setpos(0,0)
    #     self.write("GAME OVER", align="center", font=("Lemon", 20, "normal"))
    
    def reset(self):
        if self.game_score > self.high_score:
            self.high_score = self.game_score
            with open(FILE, "w") as file:
                file.write(f"{self.high_score}")
        self.game_score = 0
        self.update_score()