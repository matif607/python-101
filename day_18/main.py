from turtle import Turtle, Screen, colormode
import random
import heroes

# import turtle
# tim = turtle.Turtle()

# import turtle as t
# tim = t.Turtle()

# from turtle import *

leonard = Turtle()

leonard, colormode()


def change_color():
    R = random.random()
    G = random.random()
    B = random.random()

    leonard.color(R, G, B)


leonard.shape("turtle")
leonard.color("red")

# for _ in range(4):
#     leonard.forward(100)
#     leonard.left(90)
#
# for _ in range(10):
#     leonard.forward(10)
#     leonard.pu()
#     leonard.forward(10)
#     leonard.pendown()


# def draw_shape_up(num_of_sides):
#     angle = 360 / num_of_sides
#     change_color()
#     for _ in range(num_of_sides):
#         leonard.forward(100)
#         leonard.left(angle)
#
#
# def draw_shape_down(num_of_sides):
#     angle = 360 / num_of_sides
#     change_color()
#     for _ in range(num_of_sides):
#         leonard.forward(100)
#         leonard.right(angle)
#
#
# for n in range(3, 11):
#     draw_shape_up(n)
#
#
# for n in range(3, 11):
#     draw_shape_down(n)

direction = [0, 90, 180, 270, 360]

# for _ in range(200):
#     change_color()
#     leonard.width(10)
#     leonard.forward(50)
#     leonard.setheading(random.choice(direction))


# for _ in range(72):  # tilt is 5 deg so in 72 turns it will make a complete circle
#     leonard.speed("fastest")
#     change_color()
#     leonard.circle(100)
#     leonard.left(5)


leonard.speed("fastest")

# alternative method of drawing a spirograph
def draw_spirograph(tilt):
    for _ in range(int(360 / tilt)):
        change_color()
        leonard.circle(100)
        leonard.setheading(leonard.heading() + tilt)



draw_spirograph(5)



screen = Screen()
screen.exitonclick()
