from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500,height=300)





# Label
my_label = Label(text="I am a label",font=("Arial",24,"bold"))
my_label.pack()







# Entry
input = Entry(width=10)
input.pack()



# button functions
def click_button():
    print("BUtton Clicked")
    # my_label["text"] = "Button Clicked"
    my_label['text'] = input.get()

# Button
button = Button(text="click me",command=click_button)
button.pack()



# Last Line
window.mainloop()
