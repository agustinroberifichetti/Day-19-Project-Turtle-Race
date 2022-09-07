from turtle import Turtle, Screen
import random as rd

is_race_on = False
screen = Screen()
screen.setup(width=600, height=400)

user_bet = screen.textinput("Make your bet!", "Which turtle will win the race? Enter a color:")
                                              
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

all_turtles = []

y_position = -100
for color in colors:
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtle.penup()
    turtle.goto(-280, y_position)
    all_turtles.append(turtle)
    y_position += 40

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        turtle.forward(rd.randint(2, 10))
        if int(turtle.xcor()) >= 280:
            is_race_on = False
            if user_bet == turtle.pencolor():
                print(f"YOU WIN! The winner is the {turtle.pencolor()} turtle!")
            else:
                print(f"You lose. The winner is the {turtle.pencolor()} turtle.")
            break

screen.exitonclick()
