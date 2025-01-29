import turtle as t
import heroes
import random

tony = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color =  (r,g,b)
    return color

#colors = ["medium aquamarine", "DarkOrchid", "IndianRed", "LightSeaGreen", "DeepSkyBlue", "wheat", "SlateGray", "SeaGreen"]
#directions = [0, 90, 180, 270]
#tony.pensize(15)
tony.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tony.color(random_color())
        tony.circle(100)
        tony.setheading(tony.heading() + size_of_gap)
draw_spirograph(5)
#tony.circle(100)
#tony_the_turtle.shape("turtle")
#tony_the_turtle.color("red")
#tony_the_turtle.forward(100)
#tony_the_turtle.right(90)

"""
for _ in range(4):
    tony_the_turtle.forward(100)
    tony_the_turtle.left(90)
"""

"""
for _ in range(15):
    tony.forward(10)
    tony.penup()
    tony.forward(10)
    tony.pendown()
"""

"""
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tony.forward(100)
        tony.right(angle)
for shape_side_n in range(3,11):
    tony.color(random.choice(colors))
    draw_shape(shape_side_n)

"""

"""
for _ in range(200):
    #tony.color(random.choice(colors))
    tony.color(random_color())
    tony.forward(30)
    tony.setheading(random.choice(directions))
"""



screen = t.Screen()
screen.exitonclick()