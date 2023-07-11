from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# region ---------------------------- SEARCH WEBSITE ------------------------------- #
def find_password():
    website = web_entry.get().lower()
    try:
        with open("data.json", "r") as data_file:
            # read old data
            data = json.load(data_file)
            print(data[website]["password"])
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="Data File Found")
    except KeyError:
        messagebox.showerror(title="Error", message="Unable to find password associated with typed website, please "
                                                    "check the spelling of target website.")
    else:
        messagebox.showinfo(title=website, message=f"Your credentials are: \n Email: {data[website]['email']}\n "
                                                   f"Password: {data[website]['password']}")


# endregion


# region -------------------------- PASSWORD GENERATOR ----------------------------- #
def generate_pass():
    pass_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(10, 12))]
    password_symbols = [choice(symbols) for _ in range(randint(3, 6))]
    password_numbers = [choice(numbers) for _ in range(randint(3, 6))]

    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)


# endregion


# region ---------------------------- SAVE PASSWORD -------------------------------- #
def save_pass():
    web = web_entry.get().lower()
    password = pass_entry.get()
    email = email_entry.get()
    new_data = {
        web: {
            "email": email,
            "password": password,
        }
    }

    if len(web) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showerror(title="OOPS", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=web, message=f"Is this ok?\n Email: {email}\n Password: {password}")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    # read old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
                    # Update old data with new data
            else:
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                web_entry.delete(0, END)
                pass_entry.delete(0, END)


# endregion


# region ------------------------------ UI SETUP ----------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
# padlock = PhotoImage(file="logo.png")
# canvas.create_image(100, 100, image=padlock)
canvas.grid(column=1, row=0)

# region buttons
save_button = Button(text="Save", command=save_pass, width=44)
save_button.grid(column=1, columnspan=2, row=4)

generate_password = Button(text="Generate Password", command=generate_pass, width=15)
generate_password.grid(column=2, row=3)

search_button = Button(text="Search", command=find_password, width=15)
search_button.grid(column=2, row=1)
# endregion

# region entry
web_entry = Entry(width=33)
web_entry.grid(column=1, row=1)
web_entry.focus()

email_entry = Entry(width=52)
email_entry.grid(column=1, columnspan=2, row=2)
email_entry.insert(index=END, string="vishael.gaming@live.com")

pass_entry = Entry(width=33)
pass_entry.grid(column=1, row=3)
# endregion

# region labels
website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2)

pass_label = Label(text="Password: ")
pass_label.grid(column=0, row=3)
# endregion

# endregion

window.mainloop()
