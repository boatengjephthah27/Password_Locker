from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD
import random as ran, pyperclip, json


# **************************************** PASSWORD GENRATOR / FUNCTIONS ********************************************

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']
    
    password = ""
    
    letters_pass = [ran.choice(letters) for i in range(7)]
    numbers_pass = [ran.choice(numbers) for i in range(5)]
    symbols_pass = [ran.choice(symbols) for i in range(3)]
    
    passcode = letters_pass + numbers_pass + symbols_pass
    
    ran.shuffle(passcode)
        
    for value in passcode:
        password += value        
    
    Password_input.delete(0, END)
    
    Password_input.insert(0, password)
    pyperclip.copy(password)
    
    




# **************************************** SAVE DETAILS ********************************************

def save_details():
    webname = (website_input.get()).capitalize()
    username = mail_input.get()
    passname = Password_input.get()
    file_dict = {
        webname: {
            "Username": username,
            "Password": passname
        },
    }
    
    if len(webname) == 0 or len(username) == 0 or len(passname) == 0:
        messagebox.showwarning(
            title = "Empty Fields",
            message = "Fields Empty\nAll fields must be filled!"
        )
    
    else:
        validate = messagebox.askquestion(
            title = f"{webname} Logins", 
            message = f"Details Entered: \n\n Website: {webname}\n Username: {username}\n Password: {passname} \n\nDo you want to Save?"
        )
        
        if validate:
            with open("passwords.json","r") as file:
                data_file = json.load(file)
                data_file.update(file_dict)
                
            with open("passwords.json","w") as file:
                json.dump(data_file, file, indent=4)
            
            website_input.delete(0, END)
            Password_input.delete(0, END)






# **************************************** FIND DETAILS ********************************************










# **************************************** GUI ********************************************
app = Tk()
app.title("Password Manager")
app.config(padx=35, pady=50, bg="#C4DDFF")

# image
canvas = Canvas(width=300, height=300, bg="#C4DDFF", highlightthickness=0)
img = PhotoImage(file='plbg1.png')
img_label = canvas.create_image(150, 150, image=img)
canvas.grid(row=0, column=1)

# labels
website = Label(
    text="Website:",
    font= ("CURSIVE", 20), 
    bg="#C4DDFF"
)
website.grid(row=1, column=0)

mail = Label(
    text="Email/Username:",
    font= ("CURSIVE", 20), 
    bg="#C4DDFF"
)
mail.grid(row=2, column=0)

Password = Label(
    text="Password:",
    font= ("CURSIVE", 20), 
    bg="#C4DDFF"
)
Password.grid(row=3, column=0)

# inputs
website_input = Entry(
    font= ("CURSIVE", 20),
    width=28, 
    bg="#F9F9F9", 
    highlightthickness=0
)
website_input.focus()
website_input.grid(row=1, column=1)

mail_input = Entry(
    font= ("CURSIVE", 20),
    width=44, 
    bg="#F9F9F9", 
    highlightthickness=0
)
mail_input.insert(END,"boatengjephthah27@gmail.com")
mail_input.grid(row=2, column=1, columnspan=2)

Password_input = Entry(
    font= ("CURSIVE", 20),
    width=28, 
    bg="#F9F9F9", 
    highlightthickness=0
)
Password_input.grid(row=3, column=1)


# Buttons
search_Btn = Button(
    text="Search Details",
    font=("CURSIVE", 20),
    pady=3,
    highlightthickness=0,
    bg="#C4DDFF",
    border=1,
    padx=24,
    command=find
)
search_Btn.grid(row=1, column=2)

generate = Button(
    text="Generate Password",
    font=("CURSIVE", 20),
    pady=3,
    highlightthickness=0,
    bg="#C4DDFF",
    border=1,
    command=generate_password
)
generate.grid(row=3, column=2)

add = Button(
    text="Add Details",
    font=("CURSIVE", 20, BOLD),
    width=42,
    pady=6,
    highlightthickness=0,
    bg="#C4DDFF",
    border=1,
    command=save_details
)
add.grid(row=4, column=1, columnspan=2)




app.mainloop()