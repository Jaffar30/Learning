from tkinter import *
import math
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


def reset_timer():
    global timer , reps
    window.after_cancel(timer)
    timer = None
    reps = 0
    title_timer.config(text="Timer")
    canvas.itemconfig(text="00:00")
    check.config(text="")
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break)
        title_timer(text="Break",fg=RED)
    elif reps %2 == 2 :
        count_down(short_break)
        title_timer.config(text="Break",fg=RED)
    else:
        count_down(work_sec)
        title_timer.config(text="Work",fg=GREEN)

def count_down(count):
    time_min = f"0{math.floor(count/60)}" if math.floor(count/60) < 10 else math.floor(count/60)
    time_sec = f"0{count % 60}" if count % 60 < 10 else count % 60
    canvas.itemconfig(text_time  ,text=f"{time_min}:{time_sec}")
    if count > 0:
        global timer
        window.after(1000,count_down,count-1)
    else:
        start_timer()    
        add_check =""
        for _ in range(math.floor(reps/2)):
            add_check += "✔"
        check.config(text=f"{add_check}")

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)
title_timer = Label(text="Timer" , fg=GREEN , background=YELLOW,font=(FONT_NAME,50))
title_timer.grid(column=1,row=0)
canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
photo = (PhotoImage(file="./tomato.png"))
canvas.create_image(100,112,image=photo)
text_time = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=2)
Button(text="Reset",highlightthickness=0 , command=reset_timer).grid(column=0,row=3)
Button(text="Start",highlightthickness=0,command=start_timer).grid(column=2,row=3)
check = Label(text="",fg=GREEN,bg=YELLOW)
check.grid(column=1,row=4)
canvas.mainloop()