from random import randint

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rock_paper_scissors = [rock, paper, scissors]
valid_choice = True

while valid_choice:
    try:
        user_choice = input(
            "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors")
        if user_choice in ["0", "1", "2"]:
            user_choice = int(user_choice)
            valid_choice = False
        else:
            continue
    except ValueError:
        print("Wrong input, try again.")
    except TypeError:
        print("Wrong input, try again.")
    else:
        user_hand = user_choice

bot_choice = randint(0, len(rock_paper_scissors)-1)

print(rock_paper_scissors[user_hand])
print("VS")
print(rock_paper_scissors[bot_choice])

if user_choice == 0 and bot_choice == 2:
    print("User win")
elif bot_choice == 0 and user_choice == 2:
    print("Bot win")
elif user_hand > bot_choice:
    print("User win")
elif bot_choice > user_hand:
    print("Bot win")
else:
    print("Draw")
