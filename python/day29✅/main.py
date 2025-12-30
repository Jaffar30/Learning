from tkinter import *
from tkinter import messagebox
from random import choice , randint , shuffle
import pyperclip
def add():
    web = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(web) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="missing fields" , message="Their is some fields empty \nSorry, you should fill it")
    else:
        is_true = messagebox.askokcancel(title=web , message=f"Do you want to save these \nEmail: {email}\n Password: {password}")
        if is_true:
            with open("password.txt" , 'a') as data:
                data.write(f"Website: {web} - Email: {email} - Password: {password}\n")
            web_entry.delete(0,END)
            password_entry.delete(0,END)
def generate_pass():
    password_entry.delete(0,END)
    letter =  [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
    number = [ '0' , '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' ]
    symbol = [ '!' , '#' , '$' , '%' , '&' , '(' , ')' , '*' , '+' ]
    letters = [choice(letter) for _ in range(randint(8,10))]
    numbers = [choice(number) for _ in range(randint(2,4))]
    symbols = [choice(symbol) for _ in range(randint(2,4))]
    password_list = letters + symbols + numbers
    shuffle(password_list)
    password = ''.join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)


window = Tk()
window.config(padx=20,pady=20)
canvas = Canvas(height=200,width=200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100,100,image=logo)
canvas.grid(row=0,column=1)


web_label = Label(text='Website:')
web_label.grid(row=1,column=0)
email_label = Label(text='Email/Username:')
email_label.grid(row=2,column=0)
password_label = Label(text='Password:')
password_label.grid(row=3,column=0)

web_entry = Entry(width=35)
web_entry.grid(row=1,column=1,columnspan=2)
email_entry = Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"ahmed@gmail.com")
password_entry = Entry(width=20)
password_entry.grid(row=3,column=1)

generate_button = Button(text='Generate Password',command=generate_pass)
generate_button.grid(row=3,column=2)
add_button = Button(text='add',width=35,command=add)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()