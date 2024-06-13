from turtle import Turtle
import random

COLOURS = ['red', 'green', 'yellow', 'pink', 'blue']


class Car:

    def __init__(self):
        self.cars = []
        self.new_car()

    def new_car(self):
        car1 = Turtle('square')
        car1.shapesize(1, 2)
        car1.color(random.choice(COLOURS))
        car1.penup()
        car1.goto(300, random.randint(-250, 250))
        self.cars.append(car1)

    def move(self):
        for a_car in self.cars:
            a_car.setheading(180)
            a_car.forward(20)
