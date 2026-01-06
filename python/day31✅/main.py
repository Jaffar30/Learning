from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pandas.read_csv("data/french_words.csv")
except FileNotFoundError:
    org = pandas.read_csv("data/words_need_learn.csv")
    words = org.to_dict(orient="records")
else:
    words = data.to_dict(orient="records")
current ={}
start = False
def is_start():
    global start
    start = True

def new_card():
    global current , translate_word
    window.after_cancel(translate_word)
    current = random.choice(words)
    canvas.itemconfig(title,text="French", fill="black")
    canvas.itemconfig(word , text=current["French"],fill="black")
    canvas.itemconfig(bg_image,image=front_img)
    translate_word = window.after(5000,func=translate)
    
def translate():
    global current
    canvas.itemconfig(title , text="English",fill="white")
    canvas.itemconfig(word, text=current["English"],fill="white")
    canvas.itemconfig(bg_image , image=back_img)

def word_save():
    words.remove(current)
    data = pandas.DataFrame(words)
    data.to_csv("data/words_need_learn.csv" , index=False)
    new_card()

window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
translate_word = window.after(5000, func=translate)
canvas = Canvas(width=800,height=526)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
bg_image = canvas.create_image(400,263,image=front_img)
title = canvas.create_text(400,150,text="" , font=("Arial", 40 , "italic"))
word = canvas.create_text(400,263 , text="" , font=("Arial" , 60 , "bold"))
canvas.config(bg=BACKGROUND_COLOR , highlightthickness=0)
canvas.grid(row=0,column=0 ,columnspan=2)
new_card()
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img , highlightthickness=0 , command=new_card)
wrong_button.grid(row=1,column=0)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img ,  highlightthickness=0 , command=word_save)
right_button.grid(row=1,column=1)
window.mainloop()