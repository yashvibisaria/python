from tkinter import *

screen=Tk()
screen.geometry("400x400")
screen.title("Login Page")
screen.configure(bg="#353330")

def login():
    if s.get()=="A@gmail.com" and s1.get()=="1001":
        l1.config(text="Correct")
    else:
        l1.config(text="Incorrect")
   

heading=Label(screen, text="Login to the website", fg="black", bg="#c0b9b0", font=("New times roman", 15), width=37, height=2)
heading.grid(row=1, column=1, columnspan=40)

email=Label(screen, text="Enter your Email", fg="white", bg="#4f4c48", font=("New times roman", 15), width=15, height=1)
email.grid(row=2, column=1)

password=Label(screen, text="Enter your Password", fg="white", bg="#4f4c48", font=("New times roman", 15), width=17, height=1)
password.grid(row=3, column=1)

s=StringVar()
e=Entry(screen, width=35, bg="black", fg="white", textvariable=s) 
e.grid(row=2, column=2, columnspan=1, ipady=15)

s1=StringVar()
e1=Entry(screen, width=35, bg="black", fg="white", textvariable=s1) 
e1.grid(row=3, column=2, columnspan=1, ipady=15)

l1=Label(screen)
l1.grid(row=5, column=1)
# config function is used to update, change or give any style property or text to the widget later on. Widget is created earlier and if you
# want to change something later, you can use this.
b1=Button(screen, text="Submit", fg="black", bg="#c0b9b0", font=("New times roman", 14), width=17, height=2, command=login)
b1.grid(row=4, column=1, columnspan=2)
mainloop()