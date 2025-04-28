import tkinter
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
from assets.tooltip import Tooltip


# Password Generator
def generate_password():
    password_entry.delete(0, END)
    list_of_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    list_of_symbols = ["!", "@", "#", "$", "%", "&", "*", "(", ")", "-", "=", "+"]
    list_of_lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                                 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    list_of_uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                                 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    nr_numbers = random.randint(2, 4)
    nr_symbols = random.randint(2, 4)
    nr_lowercase = random.randint(4, 5)
    nr_uppercase = random.randint(4, 5)

    # Insert numbers in the password
    password_numbers = [random.choice(list_of_numbers) for _ in range(nr_numbers)]

    # Insert symbols in the password
    password_symbols = [random.choice(list_of_symbols) for _ in range(nr_symbols)]

    # Insert lowercase letters in the password
    password_lowercase = [random.choice(list_of_lowercase_letters) for _ in range(nr_lowercase)]

    # Insert uppercase letters in the password
    password_upcase = [random.choice(list_of_uppercase_letters) for _ in range(nr_uppercase)]

    #Insert every list single into the password_generated list
    password_generated = password_lowercase + password_upcase + password_numbers + password_symbols

    #Shuffling the list
    random.shuffle(password_generated)

    final_password = "".join(password_generated)

    password_entry.insert(0,f"{final_password}")


# Copiar senha
def copy_password():
    pyperclip.copy(password_entry.get())

# Save password into a file
def save_password():
    site = website_entry.get()
    email = email_entry.get()
    senha = password_entry.get()

    if len(site) != 0 and len(senha) != 0:
        is_ok = messagebox.askokcancel(title=site,
                                       message=f"These are the entries you've typed:\nEmail: {email}\nSenha: {senha}\nIs it ok to save?")
        if is_ok:
            with open("database/passwords.txt", mode="a") as senhas:
                senhas.write(f"{site} | {email} | {senha}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
            with open("database/passwords.txt") as senhas:
                consulta = senhas.read()
                print(consulta)
    else:
        messagebox.showerror(title="Error", message="Empty Fields")

# UI Setup
caminho_icone = 'lock.ico'

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
window.iconbitmap(caminho_icone)


canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(50,100, image=lock_img)
canvas.grid(row=0, column=1)


#Labels
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)

email_username_label = Label(text="Email/Username: ")
email_username_label.grid(row=2, column=0)

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)


#Entry
website_entry = Entry(width=40)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0,"")

# Frame para agrupar password_entry + generate_password_button
icone_copiar = tkinter.PhotoImage(file="copy-icon.png")

password_frame = Frame(window)
password_frame.grid(row=3, column=1, columnspan=2, pady=5)

password_entry = Entry(password_frame, width=19)
password_entry.grid(row=0, column=0)

copy_button = Button(password_frame, image=icone_copiar, command=copy_password)
copy_button.grid(row=0, column=1)
Tooltip(copy_button, "Copy button")

generate_password_button = Button(password_frame, text="Generate Password", width=14, command=generate_password)
generate_password_button.grid(row=0, column=2, padx=0)

#Buttons
add_password_button = Button(text="Add", width=34, command=save_password)
add_password_button.grid(row=4, column=1, columnspan=2)

window.mainloop()