from random import choice


def distribute_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    return choice(cards)


def calculate_score(cards):
    if len(cards) == 2 and sum(cards) == 21:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, bot_score):
    if bot_score == user_score:
        print("DRAW")
    elif bot_score > 21:
        print("Win, the bot score is over 21")
    elif user_score > 21:
        print("Loose, your score is over 21")
    elif user_score == 0:
        print("Win, you have a blackjack")
    elif bot_score == 0:
        print("Loose, the opponenet have a blackjack")
    elif user_score > bot_score:
        print("You win")
    else:
        print("You loose")


user_cards = [distribute_cards() for _ in range(2)]
bot_cards = [distribute_cards() for _ in range(2)]
bot_score = -1
app_running = True


while app_running:
    bot_score = calculate_score(bot_cards)
    user_score = calculate_score(user_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print("Computer's first cartds: ", bot_cards[0])

    if bot_score == 0 or user_score == 0 or user_score > 21:
        app_running = False
    else:
        add_card = input("Type 'y' to get another cards, else 'n': ").lower()

        if add_card == "n":
            app_running = False
        else:
            user_cards.append(distribute_cards())

while bot_score < 17 and bot_score != 0:
    bot_cards.append(distribute_cards())
    bot_score = calculate_score(bot_cards)

compare(user_score, bot_score)
