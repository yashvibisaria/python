#-------------------------------Data Types--------------------------------
#Data types means different data which we can store it in variables.
#Single data which we store in variable
#1. Numbers : Intergers(int) and decimal(float)
#2. Strings : alpahbets, special chracters, numbers also sometimes. they are always written in " ".
# though numbers come here  but they are like text so no mathematicall allowed on string
#3. Boolean values : True/False. True means yes or correct. False means No or incorrect.

#lot of data or help variable to store lot of data together following data type:
#1. List
#2. Tuple
#3 . Set
#4. Dictonary
#-----------------------------Basic Functions---------------------------------
#print() : to print amessage 
# input() :to take answer or input from user

#-----------------------------Numbers------------------------------------
#int : integer (all values -ve and +ve)
#float (decimal values)

#+, -, *(multiply), /(didvide) this will not ignore answer after decimal, //(divide) if answer in decimal it ignores the number after decimal
print(3/4)
print(3//4)

#-----------------------------Variables-----------------------------
#Variables are used to store values or data as w discussed above like numbers, strings, boolean values etc..
#syntax : variablename=value

#------------------Rules to follow while creating variable--------------
#1. variablename always begins with text not number. number can come but after
#eg : a1=3

#2. no special characters are allowed in variablesnames except _
#eg: last_name="Yashvi@123"

#3. variablenames will not have spaces eg : last name="hello". this is wrong last and name should not have space.

#4. try to give variablename according to value we are storing although we can give anyname.
#eg if we are storing marks then give variable name  marks .
#marks=60

#5. two variables cannot have same name 

#create variables and add them up and take avaerage of them
number1=3
number2=12
number3=100
#add all variables and store answer in total
total=number1+number2+number3
#now create new variable avaerge where we will divide by 3
average=total/3
print(average)

#create 2 variables and store number in them. multiply them and then divide by 100

a=6
b=20
total1=(a*b)/100
print(total1)

#-------------------------input()------------------------------
#input() is used to ask question from user
name=input("Enter your name") # name is store in name variable
print(name)

#Note : input() always takes answer as string means even if give number it will think that number is string. 
#let say we want take ask a number from user and do some mathematical calculation we cannot do directly as it is text we have to convert to int ot float.

#Note : whnever asking a number from user using input() always use either int() or float before input()
#ask user 2 numbers and add them up
n1=int(input("Enter number one"))
n2=int(input("Enter number two"))
total=n1+n2
print(total)

#percentage : (total *100)/total no of variables