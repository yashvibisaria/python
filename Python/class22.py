# Google invoice generator in python

from tkinter import *
screen=Tk()
screen.geometry("1900x900")
screen.title("Assignment 21")
screen.config(bg="white")


label=Label(screen, text="Google Invoice Generator", fg="black", font=("Arial", 30), bg="white", width=30, height=3)
label.grid(row=1, column=2, columnspan=2)

label1=Label(screen, text="Order Num:", fg="black", font=("Arial", 12), bg="white", width=8, height=3)
label1.grid(row=2, column=1,)

label2=Label(screen, text="Fried Potato:", fg="black", font=("Arial", 9), bg="white", width=8, height=3)
label2.grid(row=3, column=1,)

label3=Label(screen, text="Chk Burger:", fg="black", font=("Arial", 12), bg="white", width=8, height=3)
label3.grid(row=4, column=1,)

label4=Label(screen, text="Big King:", fg="black", font=("Arial", 12), bg="white", width=8, height=3)
label4.grid(row=5, column=1,)

label5=Label(screen, text="Chk Royal:", fg="black", font=("Arial", 12), bg="white", width=8, height=3)
label5.grid(row=6, column=1,)

label6=Label(screen, text="Veg Salad:", fg="black", font=("Arial", 12), bg="white", width=8, height=3)
label6.grid(row=7, column=1,)

label7=Label(screen, text="Drinks:", fg="blue", font=("Arial", 12), bg="white", width=8, height=3)
label7.grid(row=8, column=1,)

s=StringVar()
e=Entry(screen, width=15, bg="gray", textvariable=s)
e.grid(row=2, column=2, ipadx=10)

s1=StringVar()
e1=Entry(screen, width=15, bg="gray", textvariable=s1)
e1.grid(row=3, column=2, ipadx=10)

s2=StringVar()
e2=Entry(screen, width=15, bg="gray", textvariable=s2)
e2.grid(row=4, column=2, ipadx=10)

s3=StringVar()
e3=Entry(screen, width=15, bg="gray", textvariable=s3)
e3.grid(row=5, column=2, ipadx=10)

s4=StringVar()
e4=Entry(screen, width=15, bg="gray", textvariable=s4)
e4.grid(row=6, column=2, ipadx=10)

s5=StringVar()
e5=Entry(screen, width=15, bg="gray", textvariable=s5)
e5.grid(row=7, column=2, ipadx=10)

s6=StringVar()
e6=Entry(screen, width=15, bg="gray", textvariable=s6)
e6.grid(row=8, column=2, ipadx=10)

label8=Label(screen, text="Cost:", fg="blue", font=("Arial", 12), bg="white", width=8, height=3)
label8.grid(row=3, column=3)

label9=Label(screen, text="Service Charge:", fg="blue", font=("Arial", 12), bg="white", width=8, height=3)
label9.grid(row=4, column=3)

label10=Label(screen, text="Tax:", fg="blue", font=("Arial", 12), bg="white", width=8, height=3)
label10.grid(row=5, column=3)

label11=Label(screen, text="Subtotal:", fg="blue", font=("Arial", 12), bg="white", width=8, height=3)
label11.grid(row=6, column=3)

label12=Label(screen, text="Total:", fg="blue", font=("Arial", 12), bg="white", width=8, height=3)
label12.grid(row=7, column=3)


s7=StringVar()
e7=Entry(screen, width=15, bg="gray", textvariable=s7)
e7.grid(row=3, column=4, ipadx=10)

s8=StringVar()
e8=Entry(screen, width=15, bg="gray", textvariable=s8)
e8.grid(row=4, column=4, ipadx=10)

s9=StringVar()
e9=Entry(screen, width=15, bg="gray", textvariable=s9)
e9.grid(row=5, column=4, ipadx=10)

s10=StringVar()
e10=Entry(screen, width=15, bg="gray", textvariable=s10)
e10.grid(row=6, column=4, ipadx=10)

s11=StringVar()
e11=Entry(screen, width=15, bg="gray", textvariable=s11)
e11.grid(row=7, column=4, ipadx=10)



def price():
    global total1, total2, total3
    total1=int(e1.get())+int(e2.get())+int(e3.get())+int(e4.get())+int(e5.get())+int(e6.get())
    s7.set(total1)
    total2=total1*(6/100)
    s8.set(total2)
    total3=total1*(3/100)
    s9.set(total3)
    s10.set(total1)

def total():
    total4=total1+total2+total3
    s11.set(total4)

def refresh():
    e.delete(0, END)
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    e8.delete(0, END)
    e9.delete(0, END)
    e10.delete(0, END)
    e11.delete(0, END)
  

def exit():
    screen.destroy()


button1=Button(screen, text="Price", fg="black", font=("Arial", 12), bg="orange", width=8, height=3, command=price)
button1.grid(row=9, column=1)

button2=Button(screen, text="TOTAL", fg="black", font=("Arial", 12), bg="orange", width=8, height=3, command=total)
button2.grid(row=9, column=2)

button3=Button(screen, text="REFRESH", fg="black", font=("Arial", 12), bg="orange", width=8, height=3, command=refresh)
button3.grid(row=9, column=3)

button4=Button(screen, text="EXIT", fg="black", font=("Arial", 12), bg="orange", width=8, height=3, command=exit)
button4.grid(row=9, column=4)



mainloop()