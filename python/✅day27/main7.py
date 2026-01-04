from tkinter import *

window = Tk()
window.title("Convert Unit")
window.minsize(width=120,height=120)




# Label
miles_label = Label(text="Miles")
kilos_label = Label(text="Kilos")
space_label1 = Label(width=25)
#================================================

# input
miles_input = Entry()
kilos_input = Entry()
#================================================

# Radiobutton
def radio_used():
    print(radio_state.get())
    if radio_state.get() == 1:
        miles_label.grid(row=1,column=0)
        kilos_label.grid(row=1,column=2)
        miles_input.grid(row=2,column=0)
        kilos_input.grid(row=2,column=2)
        kilos_input.config(state='readonly')
        miles_input.config(state='normal')
    else:
        miles_label.grid(row=1,column=2)
        kilos_label.grid(row=1,column=0)
        miles_input.grid(row=2,column=2)
        kilos_input.grid(row=2,column=0)
        kilos_input.config(state='normal')
        miles_input.config(state='readonly')

#Variable to hold on to which radio button value is checked.
radio_state = IntVar(value=1)
radiobutton1 = Radiobutton(text="Miles to Kilos", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Kilos to Miles", value=2, variable=radio_state, command=radio_used)
#================================================

# button function
def convert_units():
    if radio_state.get() == 1:
        miles = float(miles_input.get())
        kilos = miles * 1.60934

        kilos_input.config(state='normal')
        kilos_input.delete(0, "end")
        kilos_input.insert(0, f"{kilos:.2f}")
        kilos_input.config(state='readonly')
    else:
        kilos = float(kilos_input.get())
        miles = kilos * 0.621371

        miles_input.config(state='normal')
        miles_input.delete(0, "end")
        miles_input.insert(0, f"{miles:.2f}")
        miles_input.config(state='readonly')




# button
button = Button(text="Convert",command=convert_units)

#================================================


# positions

# radio buttons (measures options)
radiobutton1.grid(row=0,column=0)
space_label1.grid(row=0,column=1)
radiobutton2.grid(row=0,column=2)

# labels
miles_label.grid(row=1,column=0)
kilos_label.grid(row=1,column=2)
kilos_input.config(state='readonly')

# entries
miles_input.grid(row=2,column=0)
kilos_input.grid(row=2,column=2)

# button
button.grid(row=3,column=1)







window.mainloop()