# The Reeborg's world
# url : https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json


def turn_around():
    for _ in range(3):
        turn_left()


def game():
    if not wall_on_right():
        turn_around()
        move()
    elif front_is_clear() and wall_on_right():
        move()
    else:
        turn_left()


while not at_goal():
    game()
