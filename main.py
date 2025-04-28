from tkinter import *
import pandas as pd

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# Save password into a file
def save_password():
    with open("database/passwords.txt", mode="a") as senhas:
        site = website_entry.get()
        email = email_entry.get()
        senha = password_entry.get()
        senhas.write(f"{site} | {email} | {senha}\n")
    with open("database/passwords.txt") as senhas:
        consulta = senhas.read()
        print(consulta)


# UI Setup
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=lock_img)
canvas.grid(row=0, column=1)



#Labels
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)


email_username_label = Label(text="Email/Username: ")
email_username_label.grid(row=2, column=0)


password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)


#Entry
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0,"henrysilver.gold@gmail.com")

password_entry = Entry(width=19)
password_entry.grid(row=3, column=1)

#Buttons
generate_password_button = Button(text="Generate Password", width=12)
generate_password_button.grid(row=3, column=2)

add_password_button = Button(text="Add", width=34, command=save_password)
add_password_button.grid(row=4, column=1, columnspan=2)






















window.mainloop()
