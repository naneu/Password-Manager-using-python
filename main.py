import random
import json
from tkinter import *
from tkinter import messagebox

import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    pass_letters = [random.choice(letters) for _ in range(nr_letters)]
    pass_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    pass_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = pass_letters  + pass_symbols + pass_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    pass_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    website = web_input.get()
    email = email_input.get()
    password = pass_input.get()
    new_data = {
        website:{
            "email": email,
            "password": password
            }
        }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oooops", message="Please don't leave any fields empty!!!")

    else: 
        try: 
            with open("data.json", "r") as file:
                #reading the old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            #update with the new data
            data.update(new_data)
      

            with open("data.json", "w") as file:
                #saving thr updated data
                json.dump(data, file, indent=4)
        finally: 
            web_input.delete(0, END)
            pass_input.delete(0, END)

        

#----------------------------- SEARCH FUNCTIONALITY --------------------------#
def find_password():
    website = web_input.get()
    try: 
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
            
    else: 
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword is: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

    finally: 
        web_input.delete(0, END)
        

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
pass_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image = pass_image)
canvas.grid(row=0, column=1)

#labels
web_label = Label(text="Website:")
web_label.grid(row=1,column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)

#buttons

add_btn = Button(text="Add", width=36, command=save_data)
add_btn.grid(row=4, column=1, columnspan=2)

gen_btn = Button(text="Generate Password", command=generate_password)
gen_btn.grid(row=3, column=2)

search_button = Button(text="Search",width=16,  command=find_password)
search_button.grid(row=1, column=2)

#entries

web_input = Entry(width=21)
web_input.grid(row=1, column=1)
web_input.focus()
website = web_input.get()

email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "turie@gmail.com")
email = email_input.get()

pass_input = Entry(width=21)
pass_input.grid(row=3, column=1)
password = pass_input.get()


window.mainloop()
