from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/Swedish - Common words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(language_label, text="Swedish", fill="black")
    canvas.itemconfig(word_label, text=current_card["Swedish"], fill="black")
    canvas.itemconfig(canvas_background, image=card_front_img)
    timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(language_label, text="English", fill="white")
    canvas.itemconfig(word_label, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_background, image=card_back_img)


def know():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = window.after(3000, func=flip_card)

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
canvas_background = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)

language_label = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word_label = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

right_img = PhotoImage(file="./images/right.png")
know_words_button = Button(image=right_img, command=next_card, highlightthickness=0, borderwidth=0,
                           activebackground=BACKGROUND_COLOR)
know_words_button.grid(row=1, column=1)

wrong_img = PhotoImage(file="./images/wrong.png")
dont_know_words_button = Button(image=wrong_img, command=know, highlightthickness=0, borderwidth=0,
                                activebackground=BACKGROUND_COLOR)
dont_know_words_button.grid(row=1, column=0)

next_card()

window.mainloop()
