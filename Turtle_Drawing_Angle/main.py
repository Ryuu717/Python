import turtle as t
import random

tim = t.Turtle()

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

tim.penup()
tim.setheading(100)
tim.forward(300)
tim.setheading(0)
tim.pendown()

for n in range(3, 20):
    tim.color(random.choice(colors))
    draw_shape(n)

screen = t.Screen()
screen.exitonclick()
