# importing Libraries

from tkinter import *
import random, string
import pyperclip
from password_strength import PasswordStats

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
length = Spinbox(root, from_=8, to_=100, textvariable=pass_len, width=15).pack()

#####define function

pass_str = StringVar()


def Generator():
    password = ''
    inp = inputtxt.get(1.0, "end-1c")
    if len(inp) == 0:
        for x in range(0, 4):
            password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(
                string.digits) + random.choice(string.punctuation)
        for y in range(pass_len.get() - 4):
            password = password + random.choice(
                string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
        pass_str.set(password)
        Strength_Check(password)
    else:
        for x in range(0, 4):
            password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(
                string.digits) + random.choice(inp)
        for y in range(pass_len.get() - 4):
            password = password + random.choice(
                string.ascii_uppercase + string.ascii_lowercase + string.digits + inp)
        pass_str.set(password)
        Strength_Check(password)

def Strength_Check(password):
    #inp = inputtxt.get(1.0, "end-1c")
    stats = PasswordStats(password)
    x = str(stats.strength())
    lbl.config(text = "Password Strength: " +x)

###button

Button(root, text="GENERATE PASSWORD", command = Generator()).pack(pady=5)

heading = Label(root, text='Permitted Special Characters', font='arial 10 bold').pack()

# TextBox Creation
inputtxt = Text(root, height = 1, width = 15)
inputtxt.pack()

Button(root, text="ENTER", command = Generator).pack(pady=5)

Entry(root, textvariable=pass_str).pack()

# Label Creation
lbl = Label(root, text = "")
lbl.pack()
root.mainloop()

########function to copy

def Copy_password():
    pyperclip.copy(pass_str.get())


Button(root, text='COPY TO CLIPBOARD', command=Copy_password).pack(pady=5)

# loop to run program
root.mainloop()
