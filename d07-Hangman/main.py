# tant que l'utilisateur a de la vie, il va devoir choisir une lettre
# Si la lettre est bonne, elle est remplacé dans le mot a deviner (si déja fait, le lui dire)
# Si la lettre n'est pas bonne, perds une vie

from data import hangman_words
from random import choice

life = 6
choosen_word = choice(hangman_words)
anonymous_word = ["_" for _ in range(0, len(choosen_word))]
game = True
print(choosen_word)

while game:
    print(anonymous_word)
    letter = input("Enter your letter: ")

    if letter in anonymous_word:
        print("You'r already put this letter.")

    for i in range(0, len(choosen_word)):
        if letter == choosen_word[i]:
            anonymous_word[i] = letter

    if "_" not in anonymous_word:
        print("NICE ONE")
        game = False

    if letter not in choosen_word:
        print("Not in the word")
        life -= 1
        if life == 0:
            game = False
            print("BIIIIP")
            print(f"The word was {choosen_word}")
