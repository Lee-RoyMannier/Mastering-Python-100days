import pandas as pd

data = pd.read_csv('../d26-Nato_Alphabet_Project/nato_phonetic_alphabet.csv')
data_to_dict = {letter.letter: letter.code for (index, letter) in data.iterrows()}


user_name = input("Enter your name: ").upper()

nato_transformation = [data_to_dict[letter] for letter in user_name]
print(nato_transformation)