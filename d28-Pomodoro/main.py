import tkinter as tk
from math import floor
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_after = None
check = []


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global check
    global reps
    screen.after_cancel(timer_after)
    reps = 0
    check = []

    title_label.config(text="Timer", fg=GREEN)
    checked_label.config(text="")
    canvas.itemconfig(timer, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global check
    checked = "✅"

    global reps
    reps += 1
    if reps % 2 != 0:
        title_label.config(text="WORK", fg=PINK)
        count_down(WORK_MIN*60)
    elif reps % 2 == 0 and reps != 8:
        check.append(checked)
        checked_label.config(text=' '.join(check))
        title_label.config(text="Break Time", fg=RED)
        count_down(SHORT_BREAK_MIN*60)
    else:
        title_label.config(text="Long Break", fg=GREEN)
        count_down(LONG_BREAK_MIN*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(x):
    global timer_after
    minute = floor(x / 60)
    sec = x % 60

    if minute < 10:
        minute = "0" + str(minute)
    if sec < 10:
        sec = "0" + str(sec)
    timer_count = f"{minute}:{sec}"
    canvas.itemconfig(timer, text=timer_count)
    if x > 0:
        timer_after = screen.after(1000, count_down, x-1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
screen = tk.Tk()
screen.title("Pomodoro")
screen.config(bg=YELLOW, padx=100, pady=50)

# Title Label, gonna change after x minute (rest or work)
title_label = tk.Label(screen, text="Timer", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN, pady=20)
title_label.grid(column=1, row=0)

# Image pomodoro, based by Canvas
canvas = tk.Canvas(screen, width=200, height=224, bg=YELLOW, highlightthickness=0)
image = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timer = canvas.create_text(100, 120, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start = tk.Button(text="Start", bg=YELLOW, highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

checked_label = tk.Label(screen, text="", font=(FONT_NAME, 10, "bold"), bg=YELLOW)
checked_label.grid(column=1, row=3)

reset = tk.Button(text="Reset", bg=YELLOW, highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)

screen.mainloop()