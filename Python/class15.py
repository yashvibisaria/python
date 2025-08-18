import os
import shutil
# These two libraries are file handling libraries used to perform difference functions of files like create, delete, opening a file with the
# help of functions, making changes in the file without opening the file with the help of functions.
# copy the data from one file to another or moving the data without opening the file.
# use open and read to open the file and get to know what is there in the file. 
# f=open("demo.txt")
# #print(f.read())
# write is used to make the changes inside the file without opening the file 
# f1=open("demo.txt", "a")
# print(f1.write("Hello world"))

# shutil.copy("demo.txt", "demo1.txt")
# shutil.move("demo.txt", "demo1.txt") 

# Moving will remove from previous file and also gets deleted.

# os.remove("demo1.txt")

# Exceptional handling means exceptional errors which come in the code. These errors are not syntax errors.
# These errors usually come from the user's side. That's why they are called as exceptional errors.
# Example : 0 division error, file not found error, wrong input given by the user, class not found error, internet issue, issue in the system, arrayyoutof indexetc..
# Syntax errors can be solved but if anything goes wrong on the users side, those errors cannot be solved. We use try and except for that. 
# Try and except will not solve the error, but rather make sure that instead of displaying the error message, it displays a normal message on
# screen. 
# Syntax for try and except : 
# try:
#    code which we think might create an issue
# except 
#    message to be displayed

#without try and except
a=3
b=0

# print(a/b)


#with try and except
# put that code in try which you thik might create an issue. try will first try exceuting code.
#if it works it is good, if does thne it goes to except to display error message

try:
    a=int(input("Enter first number"))
    b=int(input("Enter second number"))
    print(a/b)
except:
    print("Try again without zero")

