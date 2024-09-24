from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("data/to learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
print(data)
to_learn = data.to_dict(orient="records")
print(to_learn)
print(len(to_learn))


# -----------------------------WORD RESET LOGIC/CARD TURN-----------------------------
# logic problem. The next card is removed from "to learn" not the curren
def checkmark():
    global to_learn
    current_card = random.choice(to_learn)
    to_learn.remove(current_card)
    df = pandas.DataFrame(to_learn)
    df.to_csv("data/to learn.csv", index=False)
    print(len(to_learn))
    current_word = current_card["French"]
    canvas.itemconfig(canvas_image, image=front_image)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_text, text=current_word, fill="black")

    window.after(3000, flip_card, current_card)


def cross():
    current_card = random.choice(to_learn)
    print(len(to_learn))
    current_word = current_card["French"]
    canvas.itemconfig(canvas_image, image=front_image)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_text, text=current_word, fill="black")

    window.after(3000, flip_card, current_card)


def flip_card(current_card):
    current_word = current_card["English"]
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_text, text=current_word, fill="white")


# --------------------------------------UI SETUP--------------------------------------
window = Tk()
window.title("Flash cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Card
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
back_image = PhotoImage(file="images/card_back.png")
front_image = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=front_image)
card_title = canvas.create_text(400, 150, text="", fill="black", font=("Ariel", 26, "italic"))
card_text = canvas.create_text(400, 260, text="", fill="black", font=("Ariel", 32, "bold"))
canvas.grid_configure(row=0, column=0, columnspan=2, pady=10)

# Confirm button
checkmark_image = PhotoImage(file="images/right.png")
button_right = Button(image=checkmark_image, highlightthickness=0, command=checkmark)
button_right.grid_configure(row=1, column=1)

# Wrong button
cross_image = PhotoImage(file="images/wrong.png")
button_left = Button(image=cross_image, highlightthickness=0, command=cross)
button_left.grid_configure(row=1, column=0)

cross()

mainloop()
