from turtle import Turtle


class Tim(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('green')
        self.penup()
        self.setheading(90)
        self.goto(0, -300)

    def move(self):
        self.forward(20)
