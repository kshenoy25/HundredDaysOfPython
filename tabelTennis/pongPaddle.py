from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(350, 0)

    def go_up(self):
        # y position changes
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        # y position changes
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

class Paddle_Right(Paddle):
    def __init__(self):
        super().__init__(self)
        self.goto(350, 0)

class Paddle_Left(Paddle):
    def __init__(self):
        super().__init__(self)
        self.goto(-350, 0)