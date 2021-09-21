import random
from turtle import Turtle, Screen

IS_RACE_ON = False
screen = Screen()
screen.screensize(canvheight=500, canvwidth=600)
s_width = screen.window_width()

colors = [ "orange", "green", "yellow", "purple","blue","red",]

screen.setup(width=500, height=500)
user_bet = screen.textinput(title="make your bet", prompt="which turtle will win? input color")
print(user_bet)


def run(turtle):
    turtle.speed = random.randint(1,100)
    step = random.randint(0, 50)
    turtle.forward(step)


def goto_start_line(turtle, y, x):
    turtle.penup()
    turtle.goto(y, x)


x = -100
turtle_list = []

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    goto_start_line(new_turtle, -240, x)
    x += 50
    turtle_list.append(new_turtle)

if user_bet:
    IS_RACE_ON = True


while IS_RACE_ON:
    for turtle in turtle_list:
        turtle.forward(random.randint(5, 50))

        if turtle.xcor() > s_width/2:
            IS_RACE_ON = False
            turtle.shapesize(stretch_wid=5, stretch_len=5, outline=None)
            if turtle.pencolor() == user_bet:
                screen.textinput(title=f"You won! The {turtle.pencolor()} turtle won the race!", prompt=None)
            else:
                screen.textinput(title=f"You lost! The {turtle.pencolor()} turtle won the race!", prompt=None)




print(s_width)

screen.exitonclick()