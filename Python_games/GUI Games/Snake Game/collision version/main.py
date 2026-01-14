from turtle import Turtle,Screen
from snake import Snake
import time
from food import Food
from score import Score

window = Screen()
window.bgcolor("black")

window.tracer(0)
w = window.window_width()/2
h = window.window_height()/2

user_score = Score()
sam = Snake(3, 10)
food = Food()

head = sam.head
window.update()

def main() :
    window.listen()

    window.onkey(sam.move_right, "Right")
    window.onkey(sam.move_left, "Left")
    window.onkey(sam.move_up, "Up")
    window.onkey(sam.move_down, "Down")

    while True:
        #If the snake collides the walls, the game is over
        if  head.xcor() >= w or head.xcor() <= -w or head.ycor() >= h or head.ycor() <= -h+55:
            user_score.game_over()
            break
        sam.move()
        #The snake eats the food
        if head.distance(food) < 15 :
            if food.k == 1:
                user_score.increase_score(3)
            else:
                user_score.increase_score(1)
            food.randappear() # The food disappears from its place and appears somewhere else
            #The snake gets longer
            for _ in range(2):
                sam.add_segment()
            sam.steps +=.4 #The snake gets faster
        #If the snake ate itself, the game is over
        if sam.collision():
            user_score.game_over()
            break
        time.sleep(.013)
        window.update()

if __name__ == "__main__" :
    main()
    while window.textinput(title = "Again?", prompt = "Would you like to play again(y/n)") == "y":
        sam.reset()
        window.bgcolor("black")
        user_score.reset_score()
        main()

window.exitonclick()
