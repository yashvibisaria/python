from tkinter import *
from tkinter import messagebox
screen=Tk()
screen.geometry("600x600")
screen.title("Dropdown and checkboxes")
# Check box means which allow us to select multiple options
# Every checkbox has seperate tkinter variables. Apart from that we have onvalue and offvalue. Onvalue=1 means if the person had selected the
# checkbox, they will automatically get one tkinter variable. Offvalue=0 means the person has not selected the checkbox and we get 0 in the
# tkinter variable.
r=IntVar()
c1=Checkbutton(screen, text="Dog", onvalue=1, offvalue=0, variable=r)
c1.grid(row=3, column=1)
s=IntVar()
c2=Checkbutton(screen, text="Cat", onvalue=1, offvalue=0, variable=s)
c2.grid(row=3, column=2)
# We will check if th person had selected the checkbox or not, if its selected, it will print the message accordingly
def hello():
    if r.get()==1 and s.get()==0:
        messagebox.showinfo("Message", "Dog is selected.")
    elif r.get()==0 and s.get()==1:
        messagebox.showinfo("Message", "Cat is selected.")
    elif r.get()==0 and s.get()==0:
        messagebox.showinfo("Message", "None are selected.")
    else:
        messagebox.showinfo("Message", "Both animals are selected.")

button=Button(screen, text="Click", fg="black", bg="white", height=3, width=11, command=hello)
button.grid(row=2, column=1)
mainloop()