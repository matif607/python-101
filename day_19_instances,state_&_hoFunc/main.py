from turtle import Turtle, Screen, colormode as c
import random

race_is_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="which turtle is gonna win the race. Chose your color: ")
y_position = [0, 50, 100, -50, -100, 150, -150]
colors = ['red', 'orange', 'blue', 'green', 'yellow', 'violet', 'indigo']
all_turtles = []

for turtle_index in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    race_is_on = True

while race_is_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_is_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"Congratulations!!! You've won. The winning color is {winning_turtle}")
            else:
                print(f"Hard luck. You lost. The winning color is {winning_turtle}")
        turtle_distance = random.randint(1, 10)
        turtle.forward(turtle_distance)


screen.exitonclick()
