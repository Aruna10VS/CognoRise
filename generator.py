from tkinter import *
import string
import random

def generator():
    small_alphabet = string.ascii_lowercase
    capital_alphabets = string.ascii_uppercase
    numbers = string.digits
    special_characters = string.punctuation

    all = small_alphabet + capital_alphabets + numbers + special_characters
    password_length = int(lengthbox.get())
    passwordField.delete(0, END)

    if choice.get() == 1:
        password = random.choices(small_alphabet, k=password_length)
    elif choice.get() == 2:
        password = random.choices(small_alphabet + capital_alphabets, k=password_length) 
    elif choice.get() == 3:
        password = random.choices(all, k=password_length)

    passwordField.insert(0, "".join(password))

def copy_to_clipboard():
    root.clipboard_clear()  
    root.clipboard_append(passwordField.get())  
    root.update()  

root = Tk()
root.title("Password Generator")
root.geometry("500x400")  
choice = IntVar()

passwordLabel = Label(root, text='Password Generator', font=('times new roman', 24, 'bold'))
passwordLabel.grid(pady=10)

weakradiobutton = Radiobutton(root, text='Weak', value=1, variable=choice, font=('times new roman', 14))
weakradiobutton.grid()

mediumradiobutton = Radiobutton(root, text='Medium', value=2, variable=choice, font=('times new roman', 14))
mediumradiobutton.grid()

strongradiobutton = Radiobutton(root, text='Strong', value=3, variable=choice, font=('times new roman', 14))
strongradiobutton.grid(pady=5)

lengthLabel = Label(root, text='Enter the Password length:', font=('times new roman', 18))
lengthLabel.grid(pady=10)

lengthbox = Spinbox(root, from_=5, to=18, width=5, font=('times new roman', 14))  
lengthbox.grid(pady=5)

generateButton = Button(root, text='Generate', command=generator, font=('times new roman', 14))
generateButton.grid(pady=10)

passwordField = Entry(root, width=30, bd=2, font=('times new roman', 16)) 
passwordField.grid(pady=10)

copyButton = Button(root, text='Copy', command=copy_to_clipboard, font=('times new roman', 14))
copyButton.grid(pady=10)

root.mainloop()
