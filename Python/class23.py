from tkinter import *

screen=Tk()
screen.geometry("600x600")
screen.title("Class 23")

# List Box is a box where we show different list items whcih we can add, delete or select 
l=Listbox(screen, width=30, height=4, selectmode=MULTIPLE)
l.pack()
# By using add function we wil add items (the data which we want to put here) in the box
l.insert(0, "strawberry")
l.insert(0,"blueberry")
l.insert(0,"blackberry")
l.insert(0,"raspberry")

# delete, delete all, delete multiple, select multiple 

def delete():
    # it deletes only one selected items at a time
    l.delete(ANCHOR) # ANCHOR means the item which the mouse has clicked
    
def deleteall():
    # deletes all the items in the box
    l.delete(0, END)

def deletemultiple():
    # deletes multiple items selected
    for i in(l.curselection()):# the items which are selected, we get them suing curselection adn then apply thr for loop adn get them and delete
    # each one of them
        l.delete(i)


def selectmultiple():
    # select multiple times and display thsoe as labels
    # using curselection and for loop will get the item selected adn then diplay them as label
    result=""
    for i in(l.curselection()):
        result=result+str(l.get(i))
    l1.config(text=result)
        

def select():
    # select item at at a time
    l1.config(text=l.get(ANCHOR))

l1=Label(screen)
l1.pack()
b1=Button(screen, text="Delete", command=delete)
b1.pack()
b2=Button(screen, text="Delete All", command=deleteall)
b2.pack()
b3=Button(screen, text="Delete Multiple", command=deletemultiple)
b3.pack()
b4=Button(screen, text="Select Multiple", command=selectmultiple)
b4.pack()
b5=Button(screen, text="Select", command=select)
b5.pack()

mainloop()