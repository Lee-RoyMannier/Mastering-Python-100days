from random import randint


def get_difficulty():
    choose_difficulty = input("Choose a difficulty: Easy or Hard")
    if choose_difficulty == "easy":
        return EASY_LIFE
    return HARD_LIFE


def compare(user_guess, random_guess, difficulty):
    if user_guess < random_guess:
        print("COLD")
        return difficulty - 1
    elif user_guess > random_guess:
        print("HOT")
        return difficulty - 1
    else:
        print("Nice one")


EASY_LIFE = 10
HARD_LIFE = 5
MIN_RANDOM = 1
MAX_RANDOM = 100
app_running = True
random_number = randint(MIN_RANDOM, MAX_RANDOM)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
print("I'm thinking the asnwer : ", random_number)

difficulty = get_difficulty()
guess = 0
while guess != random_number:
    print(f"You have {difficulty} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))
    difficulty = compare(guess, random_number, difficulty)

    if difficulty == 0:
        print("The correct answer was ", random_number)
        break
    else:
        print("Guess again")
