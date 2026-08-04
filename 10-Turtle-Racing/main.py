from turtle import Screen
from race import create_turtles, start_race, colors

screen = Screen()
screen.setup(width=600, height=400)
screen.title("🐢 Turtle Grand Prix 🏁")

prediction = screen.textinput(
    "Make Your Prediction",
    f"Choose a turtle:\n{', '.join(colors)}"
)

turtles = create_turtles()

winner = start_race(turtles)

if prediction:

    prediction = prediction.lower()

    if prediction == winner:
        print(f"🎉 Congratulations! The {winner} turtle won!")
    else:
        print(f"😔 The {winner} turtle won.")

screen.exitonclick()