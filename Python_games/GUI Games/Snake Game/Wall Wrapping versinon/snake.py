from turtle import Turtle
class Snake:
    def __init__(self,steps,initial_number_of_parts):
        self.steps = steps
        self.snake_parts = []
        self.speed = 0
        self.shape_size = .75
        self.initial_number_of_parts = initial_number_of_parts

        for _ in range(self.initial_number_of_parts):
            self.create_segment()
        self.head = self.snake_parts[0]
        self.head.shapesize(.95)
        self.head.shape("circle")
        self.number_of_parts = len(self.snake_parts)

    def create_segment(self):
        new_part = Turtle(shape="square")
        new_part.shapesize(self.shape_size,self.shape_size)
        new_part.color("white")
        self.snake_parts.append(new_part)
        new_part.penup()
        new_part.speed(self.speed)
        return new_part

    def add_segment(self):
        segment = Turtle(shape = "square")
        segment.shapesize(self.shape_size, self.shape_size)
        segment.color("white")
        segment.penup()
        segment.speed(self.speed)
        segment.goto(self.snake_parts[-1].pos())
        self.snake_parts.insert(-1,segment)

    def move(self):

        # width = self.head.screen.window_width()/2
        # height = self.head.screen.window_height()/2
        if self.head.xcor() >= self.head.screen.window_width()/2 :
            self.head.goto(-self.head.screen.window_width()/2,self.head.ycor())
        elif self.head.xcor() <= -self.head.screen.window_width()/2 :
            self.head.goto(self.head.screen.window_width()/2,self.head.ycor())
        elif self.head.ycor() >= self.head.screen.window_height()/2 :
            self.head.goto(self.head.xcor(),-self.head.screen.window_height()/2+60)
        elif self.head.ycor() <= (-self.head.screen.window_height() / 2 +60):
            self.head.goto(self.head.xcor(), self.head.screen.window_height() / 2 )

        for ind in range(len(self.snake_parts) - 1, 0, -1):
            self.snake_parts[ind].goto(self.snake_parts[ind-1].pos())
        self.head.forward(self.steps)

    def move_right(self):
        """This is the function made to move the snake right"""
        self.head.setheading(0 if  self.head.heading() != 180 else 180)

    def move_left(self):
        """This is the function made to move the snake left"""
        self.head.setheading(180 if self.head.heading() != 0 else 0)

    def move_up(self):
        """This is the function made to move the snake up"""
        self.head.setheading(90 if self.head.heading() != 270 else -90)

    def move_down(self):
        """This is the function made to move the snake down"""
        self.head.setheading(-90 if self.head.heading() != 90 else 90)
    def collision(self):
        for part in self.snake_parts[1:]:
            if self.head.distance(part) < self.steps-1:
                return True
        return False

    def reset(self):
        for part in self.snake_parts:
            part.hideturtle()
            part.penup()
            part.goto(0,0)
            for part in self.snake_parts[:self.initial_number_of_parts]:
                part.showturtle()
            self.head.setheading(0)
            self.steps = 3

            self.snake_parts = self.snake_parts[:self.initial_number_of_parts]