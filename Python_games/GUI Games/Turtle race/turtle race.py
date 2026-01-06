from turtle import Turtle, Screen
import random

window = Screen()
window.bgcolor("orange")
window.title("Turtle race")

wr = Turtle()
wr.hideturtle()
class Turtles (Turtle) :
    def __init__(self,colour):
        super().__init__()
        self.shape("turtle")
        self.color(colour)
        self.penup()  # pull the pen up while drawing
        self.speed("slowest")

sam = Turtles(colour = "yellow")
jack = Turtles(colour = "blue")
john = Turtles(colour = "black")

n = 50
for turtle in [sam,jack,john]:
    turtle.goto(-300, 50 + n)
    n -=100

guess =  window.textinput("Make your bet",
                 "Guess the winner\nType a color: yellow, blue or black?").strip().lower()
while guess not in (sam.color()[0],jack.color()[0],john.color()[0]):
    guess = window.textinput("Make your bet",
                     "Guess the winner\nType a color: yellow, blue or black?").strip().lower()

def res(turtle):
    if guess != turtle.color()[0]:
        window.bgcolor("red")
        wr.write(f"You lose\n{turtle.color()[0]} won", font=("Arial", 25, "normal"), align="center")
    else:
        window.bgcolor("green")
        wr.write(f"{turtle.color()[0]} won", font=("Arial", 25, "normal"), align="center")

def over(*components) :
    for component in components:
        component.forward(random.randint(1, 10))
        if component.xcor() >= 300:
            res(component)
            return False
    return True

while over(sam,john,jack):
    continue

window.exitonclick()