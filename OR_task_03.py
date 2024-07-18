"*************** STRONG PASSWORD GENERATOR USING TKinter *******************"

from tkinter import *
import random, string

root = Tk()
root.geometry("300x400")
root.title("Strong Password Generator")

title = StringVar()
label = Label(root, textvariable=title).pack()
title.set("The strength of password : ")

def selection():
    selection = choice.get()

choice =IntVar()
r1 = Radiobutton(root, text="Poor", variable=choice, value=1, command=selection).pack(anchor=CENTER)
r2 = Radiobutton(root, text="Average", variable=choice, value=2, command=selection).pack(anchor=CENTER)
r3 = Radiobutton(root, text="Advance", variable=choice, value=3, command=selection).pack(anchor=CENTER)

labelchoice = Label(root)
labelchoice.pack()

lengthlabel = StringVar()
lengthlabel.set("Password length")
lengthtitle = Label(root, textvariable=lengthlabel).pack()

value = IntVar()
spinlength = Spinbox(root, from_=6, to_=20, textvariable=value, width=13).pack()

def callback():
    Isum.config(text=passgen())

passgenButton = Button(root, text="Generate Password", bd=5, height=2, command=callback, pady=3)
passgenButton.pack()
password = str(callback)

Isum = Label(root, text="")
Isum.pack(side=BOTTOM)

poor = string.ascii_uppercase + string.ascii_lowercase
average = string.ascii_uppercase + string.ascii_lowercase + string.digits
symbols = "!@#$%^&*.()[]-,/ "
advance = poor + average + symbols

def passgen():
    if choice.get() == 1:
        return "".join(random.sample(poor, value.get()))
    elif choice.get() == 2:
        return "".join(random.sample(average, value.get()))
    elif choice.get() == 3:
        return "".join(random.sample(advance, value.get()))
    

root.mainloop()