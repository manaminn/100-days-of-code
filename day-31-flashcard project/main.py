from tkinter import *
import random
import pandas
from pandas import *

# -------------------- CONSTANTS ----------------------#
BACKGROUND_COLOR = "#B1DDC6"

# -------------------- Get random word from csv ----------------------#
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)

    next_card()


# ------------------ flip card ------------------#
canvas = Canvas(width=800, height=526)




def flip_card():
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=card_back_img)



# ------------------ USER INTERFACE ------------------#
window=Tk()
window.title("Flash card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# front card image
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file='images/card_front.png')
card_back_img = PhotoImage(file='images/card_back.png')
canvas_image = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
title_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# right image button
right_img = PhotoImage(file='images/right.png')
known_button = Button(image=right_img, highlightthickness=0, command=is_known)
known_button.grid(column=1, row=1)

# wrong image button
wrong_img = PhotoImage(file='images/wrong.png')
unknown_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

next_card()

window.mainloop()
