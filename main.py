from tkinter import *
import random
import pandas
import time

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
print(data)
to_learn = data.to_dict(orient="records")
print(to_learn)


# list_of_dicts = [{row['French']: row['English']} for _, row in data.iterrows()]
# list_of_lists = [[row['French'], row['English']] for _, row in data.iterrows()]
# print(list_of_dicts)
# print(list_of_lists)


# ----------------------------------WORD RESET LOGIC----------------------------------
def next_card():
    current_card = random.choice(to_learn)
    current_word = current_card["French"]
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_text, text=current_word)

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
card_title = canvas.create_text(400, 150, text="BACK", fill="black", font=("Ariel", 26, "italic"))
card_text = canvas.create_text(400, 260, text="word", fill="black", font=("Ariel", 32, "bold"))
canvas.grid_configure(row=0, column=0, columnspan=2, pady=10)

# Confirm button
checkmark_image = PhotoImage(file="images/right.png")
button_right = Button(image=checkmark_image, highlightthickness=0, command=next_card)
button_right.grid_configure(row=1, column=0)

# Wrong button
cross_image = PhotoImage(file="images/wrong.png")
button_left = Button(image=cross_image, highlightthickness=0, command=next_card)
button_left.grid_configure(row=1, column=1)

next_card()

mainloop()
