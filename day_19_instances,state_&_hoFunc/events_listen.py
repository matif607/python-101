from turtle import Turtle, Screen, colormode
import random

screen = Screen()
leonard = Turtle()


def head_forward():
    leonard.forward(10)

def head_backward():
    leonard.backward(10)

def turn_left():
    leonard.left(10)


def turn_right():
    leonard.right(10)


def clear():
    leonard.clear()
    leonard.penup()
    leonard.home()






screen.listen()
screen.onkey(key='d', fun=head_forward)
screen.onkey(key='a', fun=head_backward)
screen.onkey(key='w', fun=turn_left)
screen.onkey(key='s', fun=turn_right)
screen.onkey(key='c', fun=clear)


leonard, colormode()


def change_color():
    R = random.random()
    G = random.random()
    B = random.random()

    leonard.color(R, G, B)


leonard.shape("turtle")
leonard.color("red")

screen.exitonclick()
