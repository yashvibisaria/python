from tkinter import *
from PIL import ImageTk, Image

screen=Tk()
screen.title("assignment 18")
screen.geometry("400x400")

screen.configure(bg="#D9B0CC")

def previous():
    a=Image.open("dogimg.png")
    a=a.resize((200,100))
    a=ImageTk.PhotoImage(a)
    l1=Label(screen, image=a)
    l1.Image=a
    l1.grid()

def next():
    b=Image.open("flowers.jpg")
    b=b.resize((200, 100))
    b=ImageTk.PhotoImage(b)
    l2=Label(screen, image=b)
    l2.Image=b
    l2.grid()


button1=Button(screen, text="  ", fg="black", bg="#ff6bbc", font=("Times New Roman", 15), width=15, height=2, command=previous)
button1.grid(row=2, column=3)

button2=Button(screen, text="  ", fg="white", bg="#ff6bbc", font=("Times New Roman", 15), width=15, height=2, command=next)
button2.grid(row=3, column=3)


mainloop()