# importing Libraries

from tkinter import *
import random, string
import pyperclip

###initialize window

root = Tk()
root.geometry("400x400")
root.resizable(0, 0)
root.title("YAY - PASSWORD GENERATOR")

# heading
heading = Label(root, text='PASSWORD GENERATOR', font='arial 15 bold').pack()

###select password length
pass_label = Label(root, text='PASSWORD LENGTH', font='arial 10 bold').pack()
pass_len = IntVar()
length = Spinbox(root, from_=8, to_=32, textvariable=pass_len, width=15).pack()

#####define function




###button

Button(root, text="GENERATE PASSWORD", command=Generator).pack(pady=5)

Entry(root, textvariable=pass_str).pack()


########function to copy

def Copy_password():
    pyperclip.copy(pass_str.get())


Button(root, text='COPY TO CLIPBOARD', command=Copy_password).pack(pady=5)

# loop to run program
root.mainloop()
