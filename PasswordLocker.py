from tkinter import *

# **************************************** PASSWORD GENRATOR ********************************************







# **************************************** SAVE DETAILS ********************************************








# **************************************** GUI ********************************************
app = Tk()
app.title("Password Manager")
app.config(padx=30, pady=50)

# image
canvas = Canvas(width=300, height=300)
img = PhotoImage(file='plbg1.png')
img_label = canvas.create_image(150, 150, image=img)
canvas.grid(row=0, column=1)

# labels
website = Label(
    text="Website:",
    font= ("COURIER", 20)
)
website.grid(row=1, column=0)

mail = Label(
    text="Email/Username:",
    font= ("COURIER", 20)
)
mail.grid(row=2, column=0)

Password = Label(
    text="Password:",
    font= ("COURIER", 20)
)
Password.grid(row=3, column=0)

# inputs
website_input = Entry(
    font= ("COURIER", 18),
    width=40
)
website_input.grid(row=1, column=1, columnspan=2)

mail_input = Entry(
    font= ("COURIER", 18),
    width=40
)
mail_input.grid(row=2, column=1, columnspan=2)

Password_input = Entry(
    font= ("COURIER", 18),
    width=40
)
Password_input.grid(row=3, column=1)


# Buttons
generate = Button(
    text="Generate Password",
    font=("COURIER", 18),
    pady=3
)
generate.grid(row=3, column=2)

add = Button(
    text="Add Details",
    font=("COURIER", 18),
    padx=280,
    pady=10
)
add.grid(row=4, column=0, columnspan=3)




app.mainloop()