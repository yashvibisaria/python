from tkinter import *
from tkinter import messagebox

s=Tk()
s.geometry("400x400")
s.title("Assignment 19")
s.configure(bg="white")

label=Label(s, text="This is the root window.", fg="black", bg="white", font=("Arial", 13), width=18, height=2)
label.grid(row=2, column=3)

def toplevel1():
    s2=Tk()
    s2.title("Toplevel1")
    s2.geometry("400x400")
    def toplevel2():
        s3=Tk()
        s3.title("Toplevel2")
        s3.geometry("400x400")  
        label2=Label(s3, text="This is a Toplevel2 window.", fg="black", bg="white", font=("Arial", 10), width=18, height=2)
        label2.grid(row=2, column=3)
        button3=Button(s3, text="Exit", fg="white", bg="pink", command=s3.destroy)
        button3.grid(row=3, column=3)
    
    label1=Label(s2, text="This is a Toplevel1 window.", fg="black", bg="white", font=("Arial", 10), width=18, height=2)
    label1.grid(row=2, column=3)
    button2=Button(s2, text="open toplevel2", fg="black", bg="#ff6bbc", font=("Arial", 15), width=15, height=2, command=toplevel2)
    button2.grid(row=4, column=3)
    button3=Button(s2, text="Exit", fg="white", bg="pink", command=s2.destroy)
    button3.grid(row=5, column=3)



button1=Button(s, text="open toplevel1", fg="black", bg="#ff6bbc", font=("Arial", 15), width=15, height=2, command=toplevel1)
button1.grid(row=3, column=3)

mainloop()