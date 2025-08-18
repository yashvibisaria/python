from tkinter import *
from tkinter import messagebox
s=Tk()
s.geometry("400x400")
s.title("Message box and frame properties")

# Message box means the pop up messages which appear on screen 
# Steps
# 1. Import message box at the top
# 2. Use different message box functions

# According to your requirement you can use it.
# For simple message
messagebox.showinfo("info", "the information is correct")
# For error and warning messages
messagebox.showerror("error", "There was an error by downloading the file")
messagebox.showwarning("warning", "There was an error while downloading the file")
# To ask questions there are four functions
# Difference is in their name of the buttons.
messagebox.askokcancel("Ask a question", "Do you want to download this file?")
messagebox.askretrycancel("Ask a question", "Do you want to download this file?")
messagebox.askyesno("Ask a question", "Do you want to download this file?")
messagebox.askyesnocancel("Ask a question", "Do you want to download this file?")

def secondscreen():
    s2=Tk()
    s2.title("")
    s2.geometry("400x400")
    button=Button(s2, text="Hello", fg="white", bg="pink", command=s2.destroy)
    button.grid(row=2, column=3)

button=Button(s, text="", fg="black", bg="#ff6bbc", font=("Times New Roman", 15), width=15, height=2, command=secondscreen)
button.grid(row=2, column=3)
# To create a new screen, we have to use the same Tk function and set the title and geometry, but all we things we have to do in a function and
# then call that function into a button so that when the button is clicked it takes us to the second screen







mainloop()