from art import logo, vs
from game_data import data
from random import choice
import os


def display_info(personality):
    name = personality["name"]
    description = personality["description"]
    coutry = personality["country"]

    return f"{name}, a {description}, from {coutry}"


def compare_followers(personality_one, personality_two, answer):
    if personality_one["follower_count"] > personality_two["follower_count"]:
        return answer == "A"
    return answer == "B"


app_running = True
first_compare = choice(data)
next_compare = choice(data)
print(logo)
score = 0

if first_compare == next_compare:
    next_compare = choice(data)

while app_running:
    first_compare = next_compare
    next_compare = choice(data)
    if first_compare == next_compare:
        next_compare = choice(data)
    print(f"Compare A: {display_info(first_compare)}")
    print(vs)
    print(f"Compare B: {display_info(next_compare)}")
    user_answer = input("Who has more followers? Type 'A' or 'B'").upper()
    print("\n" * 20)
    print(logo)
    if compare_followers(first_compare, next_compare, user_answer):
        score += 1
        print(f"Current score: {score}")
    else:
        app_running = False
        os.system("clear")
        print(logo)
        print(f"You're wrong, Final score: {score}")
