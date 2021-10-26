from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("HighScore.txt", mode="r") as hs:
            self.high_score = int(hs.read())
        self.pu()
        self.ht()
        self.goto(0, 265)
        self.color("white")
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset_hs(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("HighScore.txt", mode="w") as hs:
                hs.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    def increment_score(self):
        self.score += 1
        self.update_score()
