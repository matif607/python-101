# import colorgram as c
import random
import turtle as t

color_list = [(104, 106, 125), (213, 152, 91), (140, 140, 150), (186, 62, 32), (225, 212, 109), (199, 147, 173),
              (237, 215, 225), (105, 112, 170), (177, 159, 47), (218, 224, 219), (186, 19, 9), (38, 40, 21),
              (27, 25, 63), (26, 42, 22), (223, 167, 194), (42, 44, 101), (205, 87, 58), (58, 68, 54), (132, 136, 132),
              (190, 187, 218), (230, 176, 172), (231, 65, 82)]

change_color = random.choice(color_list)
print(change_color)


dontallo = t.Turtle()
screen = t.Screen()
color = t.colormode(255)

screen.setworldcoordinates(-1, -1, screen.window_width() - 1, screen.window_height() - 1)

dontallo.shape("turtle")
dontallo.color("red")

dontallo.dot(20, random.choice(color_list))
dontallo.penup()
dontallo.forward(50)
dontallo.dot(20, random.choice(color_list))
dontallo.forward(50)



screen.exitonclick()

#
# rgb_colors = []
# colors = c.extract('image.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)



