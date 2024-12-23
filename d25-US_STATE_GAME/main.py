from turtle import Turtle, Screen
import pandas as pd

def get_coord_by_country(country, data):
    x = data[data["state"] == country].x.tolist()[0]
    y = data[data["state"] == country].y.tolist()[0]
    coord_country = (x, y)
    print(coord_country)

    return coord_country


data = pd.read_csv('../d25-US_STATE_GAME/50_states.csv')
nb_country = len(data.state.unique())
response = 0

screen = Screen()
screen.setup(width=725, height=491)
screen.bgpic("../d25-US_STATE_GAME/blank_states_img.gif")

while response < nb_country:
    input_user = screen.textinput(f"{response}/{nb_country} States Correct",
                                  "What's another state name? ").title()

    if input_user in data.state.unique():
        coord = get_coord_by_country(input_user, data)
        country = Turtle()
        country.hideturtle()
        country.penup()
        country.goto(coord)
        country.write(f"{input_user.capitalize()}", font=("Arial", 10, "bold"))
        response += 1



screen.exitonclick()