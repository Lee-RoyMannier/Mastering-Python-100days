import tkinter as tk
from tkinter import messagebox
from random import choice, shuffle


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
    password = []

    nr_letters = 8
    nr_symbols = 4
    nr_numbers = 5

    for _ in range(nr_letters):
        password += choice(letters)

    for _ in range(nr_symbols):
        password += choice(symbols)

    for _ in range(nr_numbers):
        password += choice(numbers)

    shuffle(password)
    shuffled_pwd = "".join(password)
    password_entry.insert(0, shuffled_pwd)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_label.get()
    email = email_entry.get()
    pwd = password_entry.get()

    if website == "" or email == "" or pwd == "":
        messagebox.showerror("Error", "Please enter a valid input")
    else:
        is_valided = messagebox.askquestion(
            "Validation informations", "Do you want to register your new account? "
        )
        if is_valided == "yes":
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {pwd}\n")

            website_label.delete(0, tk.END)
            password_entry.delete(0, tk.END)


# ---------------------------- UI SETUP ------------------------------- #

screen = tk.Tk()
screen.title("Password Manager")
screen.config(background="white", padx=20, pady=20)

# Creation of the logo
canvas = tk.Canvas(screen, width=200, height=200, bg="white", highlightthickness=0)
image_logo = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image_logo)
canvas.grid(column=1, row=0)

# Creation website zone
label_website = tk.Label(screen, text="Website", bg="white", fg="black")
label_website.grid(column=0, row=1)
website_label = tk.Entry(screen, bg="white", fg="black", highlightthickness=0, width=35)
website_label.focus()
website_label.grid(column=1, row=1, columnspan=2, sticky="EW")

# Username zone
email = tk.Label(screen, text="Email/Username", bg="white", fg="black")
email.grid(column=0, row=2)
email_entry = tk.Entry(screen, bg="white", fg="black", highlightthickness=0, width=35)
email_entry.insert("0", "test@test.fr")
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")

# Password
password_label = tk.Label(screen, text="Password", bg="white", fg="black")
password_label.grid(column=0, row=3, sticky="EW")
password_entry = tk.Entry(
    screen, bg="white", fg="black", highlightthickness=0, width=21
)
password_entry.grid(column=1, row=3)

btn_generate_pwd = tk.Button(
    text="Generate Password", bg="white", fg="black", command=generate_password
)
btn_generate_pwd.grid(column=2, row=3, sticky="EW")

# Add final button
add_btn = tk.Button(
    screen, text="Add", bg="white", fg="black", width=36, command=save_data
)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")
screen.mainloop()
