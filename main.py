from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
# ------------------READ CSV WITH PANDAS, TURN INTO A LIST OF DICTIONARIES------------------
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")

# print(data)
to_learn = data.to_dict(orient="records")
print(to_learn)

# --------------------------------WORD RESET LOGIC/CARD TURN--------------------------------
current_card = {}
flip_timer = None
# function that gets called at the start, when the button "cross" is pressed, and after checkmark() function
def next_card():
    global current_card, flip_timer

    if flip_timer:
        window.after_cancel(flip_timer)
    try:
        current_card = random.choice(to_learn)
    except IndexError:
        print("No more cards!")
    else:
        # print(len(to_learn))
        current_word = current_card["French"]
        canvas.itemconfig(canvas_image, image=front_image)
        canvas.itemconfig(card_title, text="French", fill="black")
        canvas.itemconfig(card_text, text=current_word, fill="black")

    flip_timer = window.after(3000, flip_card, current_card)



# function that gets called when the button "checkmark" is pressed. The card gets removed from the cards "to learn".
def checkmark():
    global to_learn, current_card
    print(type(current_card))
    print(current_card)
    to_learn.remove(current_card)
    df = pandas.DataFrame(to_learn)
    df.to_csv("data/words_to_learn.csv")
    next_card()


# flip card gets called after a set time, after a new card has been selected, so that the translated text is shown.
def flip_card(current_card):
    current_word = current_card["English"]
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_text, text=current_word, fill="white")


# -----------------------------------------UI SETUP-----------------------------------------
window = Tk()
window.title("Flash cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Card
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
back_image = PhotoImage(file="images/card_back.png")
front_image = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=front_image)
card_title = canvas.create_text(400, 150, text="", fill="black", font=("Ariel", 34, "italic"))
card_text = canvas.create_text(400, 260, text="", fill="black", font=("Ariel", 66, "bold"))
canvas.grid_configure(row=0, column=0, columnspan=2, pady=10)

# Confirm button
checkmark_image = PhotoImage(file="images/right.png")
button_right = Button(image=checkmark_image, highlightthickness=0, command=checkmark)
button_right.grid_configure(row=1, column=1)

# Wrong button
cross_image = PhotoImage(file="images/wrong.png")
button_left = Button(image=cross_image, highlightthickness=0, command=next_card)
button_left.grid_configure(row=1, column=0)

next_card()

mainloop()
