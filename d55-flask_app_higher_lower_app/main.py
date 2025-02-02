from flask import Flask
from random import randint

random_number = randint(1, 10)
app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Guess a number between 1 and 10</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


@app.route("/<int:number>")
def guess_number(number):
    if number < random_number:
        return "<h1>Too Low, Try again!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    elif number > random_number:
        return "<h1>Too High, Try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    return "<h1>Nice One, You found me!</h1>" \
           "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


if __name__ == '__main__':
    app.run()
