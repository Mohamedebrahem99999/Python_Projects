from turtle import Turtle, Screen
import random
def main():
    window = Screen()
    window.bgcolor("lightblue")
    window.title("Unit Project")

    wr = Turtle()
    wr.hideturtle()

    def turtles(turt,colour,y_coordinate):
        turt.color(colour)
        turt.penup()  # pull the pen up while drawing
        turt.goto(-320, y_coordinate)
        turt.speed("slowest")

    sam = Turtle(shape ="turtle")
    turtles(sam,"yellow",window.window_height()/2-20)

    jack = Turtle(shape ="turtle")
    turtles(jack,"blue",0)

    john = Turtle(shape ="turtle")
    turtles(john,"black",-window.window_height()/2+20)

    guess =  window.textinput("Make your bet",
                     "Guess the winner\nType a color: yellow, blue or black?").strip().lower()
    while guess not in (sam.color()[0],jack.color()[0],john.color()[0]):
        guess = window.textinput("Make your bet",
                         "Guess the winner\nType a color: yellow, blue or black?").strip().lower()

    def res(tur):
        if guess != tur.color()[0]:
            window.bgcolor("red")
            wr.write(f"You lose\n{tur.color()[0]} won", font=("Arial", 25, "normal"), align="center")
        else:
            window.bgcolor("green")
            wr.write(f"{tur.color()[0]} won", font=("Arial", 25, "normal"), align="center")

    def over(tu) :
        tu.forward(random.choice(list(range(1, 10))))
        if tu.xcor() >= 300:
            res(tu)

    while sam.xcor() < 300 and jack.xcor() < 300 and john.xcor() < 300 :
        over(john)
        if john.xcor() >= 300 :
            break
        over(sam)

        if sam.xcor() >= 300:
            break
        over(jack)
    window.exitonclick()
if __name__ == "__main__":
    main()