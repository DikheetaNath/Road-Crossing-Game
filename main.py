from turtle import Screen,Turtle
from tim import Tim
from cars import Car
from scoreboard import Score
from tkinter import messagebox
import time

# Screen Configurations
screen = Screen()
screen.screensize(600, 600)
screen.bgcolor('grey')
screen.title('cross the road')
screen.tracer(8)
screen.listen()

# creating objects
car = Car()
turtle = Tim()
score = Score()
road_lines = Turtle()

# drawing road lines
road_lines.penup()
road_lines.goto(400, 0)
road_lines.pencolor('black')
step = 0


while road_lines.xcor() != -400:
    step += 1
    if step % 2 == 0:
        road_lines.pendown()
    road_lines.goto(road_lines.xcor()-20, 0)
    road_lines.penup()


# moving turtle
screen.onkey(turtle.move, 'Up')

# essential game variables
game_is_on = True
game_loop_count = 0
speed_of_cars = 0.1

# game starts
while game_is_on:
    time.sleep(speed_of_cars)
    screen.update()

    game_loop_count += 1
    if game_loop_count % 6 == 0:
        car.new_car()
    car.move()

    # Detecting collision with cars
    for i in car.cars:
        if turtle.distance(i) < 25:
            messagebox.showinfo(message=f'You Crashed. Your final score is:{score.score}')
            game_is_on = False

    # Completing a round
    if turtle.ycor() > 295:
        turtle.goto(0, -300)
        score.update_score()
        speed_of_cars *= 0.9

screen.exitonclick()
