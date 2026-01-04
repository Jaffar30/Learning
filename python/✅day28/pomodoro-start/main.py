from tkinter import *
import math

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
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60


    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break",fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break",fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work",fg=GREEN)
        

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# its every second keep refreshing to listen to user events
# GUI Event Driven through mainloop

def count_down(count):
    print(count)

    # "01:35"

    # 300 / 60 = 5

    # 245 = 
    # 245 / 60 = 4.08333
    # round it down = 4 minutes
    # 245 % 60 then get reminder for seconds

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if len(str(count_sec)) < 2:
        count_sec = f"0{count_sec}"

    if count >= 0:
        canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
        # after 1000ms = 1 second call function count_down and pass the count argunemt to be count-1
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks +="✓"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)


def say_something(thing):
    print(thing)

# window.after(1000,say_something,"Hello")
# count_down(5)

title_label = Label(text="Timer",bg=YELLOW,fg=GREEN,font=(FONT_NAME,50))
title_label.grid(row=0,column=1)

canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img =PhotoImage(file="/home/jaffar/Desktop/my_projects/Learning/python/day28/pomodoro-start/tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(101,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))

# count_down(5)

canvas.grid(row=1,column=1)

start_button = Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(row=2,column=0)

reset_button = Button(text="Reset",highlightthickness=0,command=reset_timer)
reset_button.grid(row=2,column=2)

check_marks = Label(fg=GREEN,bg=YELLOW,font=(FONT_NAME,20))
check_marks.grid(row=3,column=1)







window.mainloop()