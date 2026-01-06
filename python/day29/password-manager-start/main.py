# * import all the classes and constants but it does not import submodules
from tkinter import *
from tkinter import messagebox
import random
import pandas

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="/home/jaffar/Desktop/my_projects/Learning/python/day29/password-manager-start/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

def add_password():
    print("It works!")
    open_file = open("data.txt", "a")
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
        return
    open_file.write(f"{website} | {email} | {password}\n")

    website_input.delete(0, END)
    password_input.delete(0, END)

    messagebox.showinfo(title="Success", message="Password added successfully!")
    # is_ok = messagebox.askokcancel(title="Title", message="Message")
    # return true or false based on user click


def generate_password():
    password_input.delete(0, END)
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()1234567890"
    password = "".join(random.choice(characters) for _ in range(12))
    password_input.insert(0, password)
    window.clipboard_clear()
    window.clipboard_append(password)
    window.update()  # keeps it in clipboard after the app closes

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_input = Entry(width=35)
website_input.focus()

website_input.grid(row=1, column=1, columnspan=2)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(END, "jaffar@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_input = Entry(width=21)
password_input.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password",command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36,command=add_password)
add_button.grid(row=4, column=1, columnspan=2)




# Start the GUI event loop
window.mainloop()