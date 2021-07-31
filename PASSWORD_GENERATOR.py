# importing Libraries

from tkinter import *
import random, string
import pyperclip
from password_strength import PasswordStats

###initialize window

root = Tk()
root.geometry("400x400")
root.resizable(0, 0)
root.configure(background='red')
root.title("YAY - PASSWORD GENERATOR")

# heading
heading = Label(root, text='PASSWORD GENERATOR', font='arial 15 bold').pack()

#Space Creation
Label(root, text="",bg="red").pack()

###select password length
pass_label = Label(root, text='PASSWORD LENGTH', font='arial 10 bold').pack()
pass_len = IntVar()
length = Spinbox(root, from_=8, to_=100, textvariable=pass_len, width=15).pack()

#Space Creation
Label(root, text="",bg="red").pack()

# Select type of Password
pass_type=Label(root, text='Choose Type Of Password:-', font='arial 10 bold').pack()

# Checkbox Creation
Checkbutton1 = IntVar()  
Checkbutton2 = IntVar()  
Checkbutton3 = IntVar()  
Button1 = Checkbutton(root, text = "Letters(e.g. Aa)", variable = Checkbutton1,onvalue = 1,offvalue = 0,height = 1,width = 20).pack() 
Button2 = Checkbutton(root, text = "Digits(e.g. 345)",variable = Checkbutton2,onvalue = 1,offvalue = 0,height = 1,width = 20).pack() 
Button3 = Checkbutton(root, text = "Symbols(@$#!?)",variable = Checkbutton3,onvalue = 1,offvalue = 0,height = 1,width = 20).pack()  

#Space Creation
Label(root, text="",bg="red").pack()

# TextBox Creation
inputtxt = Text(root, height = 1, width = 15)
inputtxt.pack()
pass_str = StringVar()
Entry(root, textvariable=pass_str).pack()

# Label Creation
lbl = Label(root, text = "",bg="red")
lbl.pack()

### define function
def Generator():
    password = ''
    if (Checkbutton1.get() == 1) & (Checkbutton2.get() == 0) & (Checkbutton3.get() == 0):
        for x in range(0,2):
            password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase)
        for y in range(pass_len.get() - 2):
            password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase)
        pass_str.set(password)
        Strength_Check(password)
    
    elif (Checkbutton1.get() == 0) & (Checkbutton2.get() == 1) & (Checkbutton3.get() == 0):
        for x in range(0, 2):
            password = random.choice(string.digits)
        for y in range(pass_len.get() - 2):
            password = password + random.choice(string.digits)
        pass_str.set(password)
        Strength_Check(password)
   
    elif (Checkbutton1.get() == 1) & (Checkbutton2.get() == 1) & (Checkbutton3.get() == 0):
        for x in range(0, 3):
            password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits)
        for y in range(pass_len.get() - 3):
            password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
        pass_str.set(password)
        Strength_Check(password)
    
    elif (Checkbutton1.get() == 1) & (Checkbutton2.get() == 0) & (Checkbutton3.get() == 1):
        inp = inputtxt.get(1.0, "end-1c")
        if len(inp) == 0:
            for x in range(0, 3):
                password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.punctuation)
            for y in range(pass_len.get() - 3):
                password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.punctuation)
            pass_str.set(password)
            Strength_Check(password)
        else:
            for x in range(0, 3):
                password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase)+ random.choice(inp)
            for y in range(pass_len.get() - 3):
                password = password + random.choice(
                    string.ascii_uppercase + string.ascii_lowercase + inp)
            pass_str.set(password)
            Strength_Check(password)
    
    elif (Checkbutton1.get() == 0) & (Checkbutton2.get() == 1) & (Checkbutton3.get() == 1):
        inp = inputtxt.get(1.0, "end-1c")
        if len(inp) == 0:
            for x in range(0, 3):
                password = random.choice(string.digits) + random.choice(string.punctuation)
            for y in range(pass_len.get() - 3):
                password = password + random.choice(string.digits + string.punctuation)
            pass_str.set(password)
            Strength_Check(password)
        else:
            for x in range(0, 3):
                password = random.choice(string.digits) + random.choice(inp)
            for y in range(pass_len.get() - 3):
                password = password + random.choice(string.digits + inp)
            pass_str.set(password)
            Strength_Check(password)
            
    elif (Checkbutton1.get() == 1) & (Checkbutton2.get() == 1) & (Checkbutton3.get() == 1):
        inp = inputtxt.get(1.0, "end-1c")
        if len(inp) == 0:
            for x in range(0, 4):
                password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)
            for y in range(pass_len.get() - 4):
                password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
            pass_str.set(password)
            Strength_Check(password)
        else:
            for x in range(0, 4):
                password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(inp)
            for y in range(pass_len.get() - 4):
                password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + inp)
            pass_str.set(password)
            Strength_Check(password)

    else:
        lbl.config(text="Please enter valid options")

#button for generating password
Button(root, text="GENERATE PASSWORD", command = Generator).pack(pady=5)

#Label for information
heading = Label(root, text='Permitted Special Characters', font='arial 10 bold').pack()

def Strength_Check(password):
    #inp = inputtxt.get(1.0, "end-1c")
    stats = PasswordStats(password)
    x = str(stats.strength())
    lbl.config(text = "Password Strength: " +x)

########function to copy
def Copy_password():
    pyperclip.copy(pass_str.get())

#Button for copy to clipboard
Button(root, text='COPY TO CLIPBOARD', command=Copy_password).pack(pady=5)

# loop to run program
root.mainloop()