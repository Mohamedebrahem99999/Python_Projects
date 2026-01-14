from turtle import Turtle,Screen
import random

class Food(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.shape("circle")
        self.color("red")
        self.penup()
        self.k = 0
        self.randappear()

    def randappear(self):
        self.k = random.randint(0, 5)
        if self.k == 1:
            self.shapesize(1,1)
        else:
            self.shapesize(.5,.5)
        self.goto(random.randint(-int(self.screen.window_width()/2)+20,int(self.screen.window_width()/2)-20),random.randint(-int(self.screen.window_height()/2)+70,int(self.screen.window_height()/2)-20))
        # self.k = random.randint(0,5)