from tkinter import *

window = Tk()
window.title("Converter")
window.config(padx=20, pady=20)

is_mile = False
is_km = False

def convert_to_mile():
    global is_mile, is_km
    space_sign.config(text="km")
    is_mile = True
    is_km = False

def convert_to_km():
    global is_mile, is_km
    space_sign.config(text="mile")
    is_mile = False
    is_km = True

def calculate_space():
    result = float(space_input.get())
    if is_mile:
        result = result / 1.609
        cal_result.config(text=f"Result: {round(result , 2)} mile")
    if is_km:
        result = result * 1.609
        cal_result.config(text=f"Result: {round(result ,2)} km")

Button(text="km to mile", command=convert_to_mile).grid(column=2, row=0)
Button(text="mile to km", command=convert_to_km).grid(column=3, row=0)

space_input = Entry()
space_input.grid(column=2, row=2)

space_sign = Label(text="unit")
space_sign.grid(column=3, row=2)

cal_result = Label(text="Type space number")
cal_result.grid(column=2, row=3)

Button(text="Calculate", command=calculate_space).grid(column=2, row=4)

window.mainloop()
