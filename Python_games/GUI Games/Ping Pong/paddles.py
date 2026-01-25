from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.position = position
        # self.screen.window_height()/2
        # self.screen.window_width()/2
        self.penup()
        self.goto(self.position)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        self.goto(self.xcor(),self.ycor()-20)
