from turtle import Turtle, Screen

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()