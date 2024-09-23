from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"


# ----------------------------------WORD RESET LOGIC----------------------------------
def chose_new_word():
    foreign_word = random.choice(data["French"])
    canvas.create_image(400, 263, image=card_image)
    canvas.create_text(400, 150, text="Title", fill="black", font=("Ariel", 26, "italic"))
    text = canvas.create_text(400, 260, text=foreign_word, fill="black", font=("Ariel", 32, "bold"))


# --------------------------------------UI SETUP--------------------------------------
window = Tk()
window.title("Flash cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Card
data = pandas.read_csv("data/french_words.csv")
data.to_dict()
print(data)
print(data["French"].to_list())
foreign_word = random.choice(data["French"])

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_image = PhotoImage(file="images/card_back.png")
canvas.create_image(400, 263, image=card_image)
canvas.create_text(400, 150, text="Title", fill="black", font=("Ariel", 26, "italic"))
canvas.create_text(400, 260, text=foreign_word, fill="black", font=("Ariel", 32, "bold"))
canvas.grid_configure(row=0, column=0, columnspan=2, pady=10)

# Confirm button
checkmark_image = PhotoImage(file="images/right.png")
button_right = Button(image=checkmark_image, highlightthickness=0, command=chose_new_word)
button_right.grid_configure(row=1, column=0)

# Wrong button
cross_image = PhotoImage(file="images/wrong.png")
button_left = Button(image=cross_image, highlightthickness=0, command=chose_new_word)
button_left.grid_configure(row=1, column=1)

mainloop()
