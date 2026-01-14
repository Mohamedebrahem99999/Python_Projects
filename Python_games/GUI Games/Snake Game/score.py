from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score = 0


        self.update_scoreboard(0)

    def update_scoreboard(self,score):
        self.clear()

        self.goto(0, (-self.screen.window_height() / 2) + 50)
        self.write("_" * 300, align="center", font=("Arial", 30, "normal")) #These two lines must be here because of the clear method

        self.score += score

        self.goto(-15, -self.screen.window_height() / 2 + 10)
        self.write(f"Score = {self.score}",align = "center", font = ("Arial", 20, "normal"))

    def increase_score(self,score):
        self.clear()
        self.update_scoreboard(score)

    def game_over(self):
        self.screen.bgcolor("red")
        self.clear()
        self.goto(0,30)
        self.write(f"Game Over",align = "center", font = ("Arial", 20, "normal"))
        self.goto(0,-30)
        self.write(f"Score = {self.score}",align = "center", font = ("Arial", 20, "normal"))
    def reset_score(self):
        self.clear()
        self.score = 0
        self.update_scoreboard(self.score)


