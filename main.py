import turtle
from turtle import Turtle, Screen


screen = Screen()

colors = ["blue", "red", "orange", "green", "yellow", "purple"]

screen.setup(width= 500, height= 500)
user_input = screen.textinput(title= "make your bet", prompt= "which turtle will win? imput color")
print(user_input)


def goto_start_line(turtle, y,x):
    turtle.penup()
    turtle.goto(y, x)

x = -100

for color in colors:
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    goto_start_line(turtle, -240, x)
    x += 50


screen.exitonclick()