# learn about Tkinter and GUI (Graghical User Interface) and Function arguments
# Tkinter module used to create GUI stuff
# Advance functions features :
# default arguments
# *args
# **kwargs

# Build a Unit converter Program using Tkinter
# Xerox PARC : created first : LAN , OOP language , GUI , develop the first mouse 

# Tk is the name of the GUI toolkit itself.

# What is Tkinter?

# Tkinter = Tcl/Tk Interface

# It is Python’s standard interface to the Tk GUI toolkit

# In simple terms:

# Tkinter lets Python talk to Tk


import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500,height=300)


# Label
my_label = tkinter.Label(text="I am a label",font=("Arial",24,"bold"))
# my_label.pack() #place it in the screen in the center top
# my_label.pack(side="bottom")
my_label.pack(expand=True)


# Last Line
window.mainloop()
