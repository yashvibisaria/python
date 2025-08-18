from tkinter import *
screen=Tk()
screen.geometry("600x600")
screen.title("Assignment 21")

r=IntVar()
c1=Checkbutton(screen, text="Pepperoni", onvalue=1, offvalue=0, variable=r)
c1.grid(row=2, column=1)


def pepperoni():
    if r.get()==1:
        label.config(text="You chose pepperoni.")
    else:
        label.config(text="You did not choose pepperoni.")


button=Button(screen, text="Select toppings", fg="black", bg="white", width=20, height=3, command=pepperoni)
button.grid(row=3, column=1)

label=Label(screen, text="  ", fg="black", bg="white", width=29, height=3)
label.grid(row=4, column=1)

mainloop() 