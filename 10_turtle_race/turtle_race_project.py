from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=500)
user_bet = screen.textinput(title="Make your bet", prompt='Which turtle will win the race? Enter a color: ')
colors = ['red','orange','yellow','green', 'blue','purple']


x_coord = -230
y_coord = -100

all_turtles = []

for color in colors:
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(x=x_coord, y=y_coord)
    all_turtles.append(new_turtle)
    y_coord += 60

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()