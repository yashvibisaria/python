from tkinter import *

screen=Tk()
screen.geometry("600x600")
screen.title("Calculator")
screen.configure(bg="#353330")

#-----------------------------------4 functions will be created------------------------------
#when press any button number, sign goes in Entrybox
expression=""
def press(num):
    global expression
    # we put everything in s using set() as s is connected to e. so tempory we take num vriable whcoh we put in s
    #later when w ecall function we replace with actual.
    #eg : if we write s.set(2) then only 2 will go inside extrybox for this function thne w ehav eto create function
    #for every button. we are using one function for every button
    #also join new number with previous number using +
    expression=expression + str(num) # expression prev number + num new number 
    s.set(expression) # give this to s


#equal function
def equal():
    global expression#we use eval() whcih is  inbuilt fuction performs all mathmetical operations
    result=eval(expression)
    s.set(result) # give answer to s and it will give it to e
    expression="" # for new calculation


#clear function
def clearr():
    global expression
    expression=""
    s.set(expression)


#negative/positive function
def negative_positive():
    global expression
    expression *= -1
    s.set(expression) 


#-------------------------------------call functions------------------------------------------
#1. Non parameter function :  command =functioname
#2. Paramter function(when we pass variable in ()) : command=lambda : functionname(values)

#-------------------------------tkinter  variable--------------------------------------------
#They are just liek simplevariables used to store values. this tkinter variabkes will only store values 
#coming from widgets eg : user does anything on screen with widget or give input in entry, checkbutton, radiobutton etc.. thereanswer is stored in tkinter variables.
#we can use 4 functions to create : IntVar(), DoubleVar(), StringVar(), BoolVar()
#syntax : variablename=StringVar()
#connect the  tkinter variable with widget : textvariable=variablename or variable=variablename

#so when user enters anything in entrybox it comes in tkinter variable. and vice versa if we put anything in tkinter variable it will goto
#Entrybox as well. using set() we can put anything from tkinter var to entrybox

#We always create StringVar() for entrybox  although we give numbers because anything given in entrybox is string.
#Just like when we use input() it always takes answer a string w e have to convert

#anything we put in s using set() will goto e automatically.
#------------------------------------------------------------------------------------------------

s=StringVar()
e=Entry(screen, width=55, bg="black", textvariable=s) #Entry box doesn't have a height property, to give space inside the box we use ipadx and ipady and to give space outside
# the box or any widget padx and pady. iPadx is to give space from left right (increasing width), and ipady for increasing height
e.grid(row=1, column=1, columnspan=4, ipady=20)# wil combine 4 columns
 
clear=Button(screen, text="C", fg="white", bg="#4f4c48", font=("New times roman", 30), width=3, height=1, command=clearr)
clear.grid(row=2, column=1)

b2=Button(screen, text="+/-", fg="white", bg="#4f4c48", font=("New times roman", 30), width=3, height=1, command=negative_positive)
b2.grid(row=2, column=2)

percent=Button(screen, text="%", fg="white", bg="#4f4c48", font=("New times roman", 30), width=3, height=1, command=lambda : press("%"))
percent.grid(row=2, column=3)

divide=Button(screen, text="÷", fg="white", bg="#dd891c", font=("New times roman", 30), width=3, height=1,  command=lambda : press("÷"))
divide.grid(row=2, column=4)

multiply=Button(screen, text="x", fg="white", bg="#dd891c", font=("New times roman", 30), width=3, height=1, command=lambda : press("x"))
multiply.grid(row=3, column=4)

minus=Button(screen, text="-", fg="white", bg="#dd891c", font=("New times roman", 30), width=3, height=1,  command=lambda : press("-"))
minus.grid(row=4, column=4)

plus=Button(screen, text="+", fg="white", bg="#dd891c", font=("New times roman", 30), width=3, height=1,  command=lambda : press("+"))
plus.grid(row=5, column=4)

seven=Button(screen, text="7", fg="white", bg="#7b7772", font=("New times roman", 30), width=3, height=1,  command=lambda : press("7"))
seven.grid(row=3, column=1)

four=Button(screen, text="4", fg="white", bg="#7b7772", font=("New times roman", 30), width=3, height=1,  command=lambda : press("4"))
four.grid(row=4, column=1)

one=Button(screen, text="1", fg="white", bg="#7b7772", font=("New times roman", 30), width=3, height=1,  command=lambda : press("1"))
one.grid(row=5, column=1)

zero=Button(screen, text="0", fg="white", bg="#7b7772", font=("New times roman", 30), width=7, height=1,  command=lambda : press("0"))
zero.grid(row=6, column=1, columnspan=2)

eight=Button(screen, text="8", fg="white", bg="#7b7772", font=("New times roman", 30), width=3, height=1, command=lambda : press("8") )
eight.grid(row=3, column=2)

five=Button(screen, text="5", fg="white", bg="#7b7772", font=("New times roman", 30), width=3, height=1,  command=lambda : press("5"))
five.grid(row=4, column=2)

two=Button(screen, text="2", fg="white", bg="#7b7772", font=("New times roman", 30), width=3, height=1,  command=lambda : press("2"))
two.grid(row=5, column=2)

nine=Button(screen, text="9", fg="white", bg="#7b7772", font=("New times roman", 30), width=3, height=1,  command=lambda : press("9"))
nine.grid(row=3, column=3)

six=Button(screen, text="6", fg="white", bg="#7b7772", font=("New times roman", 30), width=3, height=1,  command=lambda : press("÷" "6"))
six.grid(row=4, column=3)

three=Button(screen, text="3", fg="white", bg="#7b7772", font=("New times roman", 30), width=3, height=1,  command=lambda : press("3"))
three.grid(row=5, column=3)

point=Button(screen, text=".", fg="white", bg="#7b7772", font=("New times roman", 30), width=3, height=1, command=lambda : press("."))
point.grid(row=6, column=3)

equalsign=Button(screen, text="=", fg="white", bg="#7b7772", font=("New times roman", 30), width=3, height=1, command=equal)
equalsign.grid(row=6, column=4)

mainloop()