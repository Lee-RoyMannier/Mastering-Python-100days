import tkinter as tk
from random import choice
import pandas as pd

current_card = {}
words_know = []


def dont_know():
    words_know.append(current_card)
    data_df.remove(current_card)
    words = pd.DataFrame(words_know)
    words.to_csv('data/words_to_learn.csv', index=False)
    get_random_word()
def get_random_word():
    global id_after, current_card
    screen.after_cancel(id_after)
    current_card = choice(data_df)
    canvas.itemconfig(word, text=current_card["English"], fill="black")
    canvas.itemconfig(language, text="English", fill="black")
    canvas.itemconfig(card_front, image=image_front)
    id_after = screen.after(3000, return_card)


def return_card():
    canvas.itemconfig(card_front, image=image_back)
    canvas.itemconfig(word, text=current_card["French"], fill="white")
    canvas.itemconfig(language, text="French", fill="white")


BACKGROUND_COLOR = "#B1DDC6"

try:
    data_df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data_df = pd.read_csv("data/french_words.csv").to_dict(orient="records")
else:
    data_df = data_df.to_dict(orient="records")
screen = tk.Tk()
screen.title("Flashy APP")
screen.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

 # Creation of the flashCard
canvas = tk.Canvas(screen, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
image_front = tk.PhotoImage(file="images/card_front.png")
image_back = tk.PhotoImage(file="images/card_back.png")
card_front = canvas.create_image(400, 263, image=image_front)
language = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"), fill="black")
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), fill="black")
canvas.grid(row=0, column=0, columnspan=2)

# Creation wrong button
image_wrong = tk.PhotoImage(file="images/wrong.png")
wrong_btn = tk.Button(image=image_wrong, highlightthickness=0, command=dont_know)
wrong_btn.grid(row=1, column=0)

# Creation button right
image_right = tk.PhotoImage(file="images/right.png")
right_btn = tk.Button(image=image_right, highlightthickness=0, command=get_random_word)
right_btn.grid(row=1, column=1)
id_after = screen.after(3000, return_card)
get_random_word()

screen.mainloop()
