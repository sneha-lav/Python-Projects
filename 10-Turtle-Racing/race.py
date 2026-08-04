import random
from turtle import Turtle

colors = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "purple"
]


def create_turtles():

    turtles = []

    y = -125

    for color in colors:

        turtle = Turtle("turtle")
        turtle.color(color)
        turtle.penup()
        turtle.goto(-230, y)

        turtles.append(turtle)

        y += 50

    return turtles


def start_race(turtles):

    winner = None

    race_on = True

    while race_on:

        for turtle in turtles:

            turtle.forward(random.randint(1, 10))

            if turtle.xcor() >= 230:

                winner = turtle.pencolor()

                race_on = False

                break

    return winner