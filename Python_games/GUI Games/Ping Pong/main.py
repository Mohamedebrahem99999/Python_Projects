from turtle import Turtle, Screen
from paddles import Paddle
from ball import Ball

window = Screen()
window.setup(width = 800, height = 550)
width = window.window_width()/2
height = window.window_height()/2
window.bgcolor("black")

paddle_right = Paddle((width-50,0))
paddle_left = Paddle((-width+50,0))
ball = Ball()
window.listen()

window.onkey(paddle_right.move_up,"Up")
window.onkey(paddle_right.move_down,"Down")
window.onkey(paddle_left.move_up,"w")
window.onkey(paddle_left.move_down,"s")

game_on = True
while game_on:
    ball.goto(ball.xcor()+.5,ball.ycor()+.25)
    if paddle_right.distance(ball) <10:
        if ball.ycor() < width:
            ball.setheading(-ball.heading())
            ball.goto(ball.xcor()+5,ball.ycor()+5)
        else :
            ball.setheading(-ball.heading())
            ball.goto(ball.xcor()-5,ball.ycor()-5)
    if ball.distance(paddle_left) < 10:
        if ball.ycor() < width :
            ball.setheading(-ball.heading())
            ball.goto(ball.xcor()+5,ball.ycor()+5)
        else :
            ball.goto(ball.xcor()-5,ball.ycor()-5)


window.exitonclick()