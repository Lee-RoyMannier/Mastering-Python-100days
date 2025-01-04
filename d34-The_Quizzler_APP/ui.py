import tkinter as tk
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class UiMainWindow():
    def __init__(self, quizz):
        self.quizz_brain = quizz
        self.active_color = None

        self.screen = tk.Tk()
        self.screen.title("Quizzler APP")
        self.screen.config(background=THEME_COLOR, padx=20, pady=20)

        self.score = tk.Label(text=f"Score: {self.quizz_brain.score}", bg=THEME_COLOR)
        self.score.grid(column=1, row=0, pady=20)

        self.canvas = tk.Canvas(width=300, height=250, highlightthickness=0, bg="black")
        self.question = self.canvas.create_text(150, 130, text="Question", fill="white", font=FONT, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        true_img = tk.PhotoImage(file="images/true.png")
        self.true_btn = tk.Button(text="Yes", bg=THEME_COLOR, image=true_img, font=FONT, command=self.true_response)
        self.true_btn.grid(column=0, row=2)
        false_img = tk.PhotoImage(file="images/false.png")
        self.false_btn = tk.Button(text="No", bg=THEME_COLOR, font=FONT, image=false_img, command=self.false_response)
        self.false_btn.grid(column=1, row=2)
        self.get_next_question()
        self.screen.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="black")
        if self.quizz_brain.still_has_questions():
            self.next_question_brain = self.quizz_brain.next_question()
            self.canvas.itemconfig(self.question, text=self.next_question_brain)
        else:
            self.canvas.itemconfig(self.question, text="No more question")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def true_response(self):
        is_right = self.quizz_brain.check_answer("true")
        self.feed_back(is_right)

    def false_response(self):
        is_right = self.quizz_brain.check_answer("false")
        self.feed_back(is_right)
    def good_response(self):
        self.canvas.config(background="green")

    def wrong_response(self):
        self.canvas.config(background="red")

    def feed_back(self, right):
        if right:
            self.good_response()
            self.score.config(text=f"score: {self.quizz_brain.score}")
        else:
            self.wrong_response()

        self.screen.after(1000, self.get_next_question)
