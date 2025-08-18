#--------------------------Strings-----------------------------
#String means alpahbets, special character, numbers written in " " eg : a123@gmail.com is string.

a="Hello this is yashvi"
print(a)

#------------String index or position value-----------------------
#code gives position number to every alphabet starts from 0. means alphabet which comes first ia at 0 position,
#alphabet which comes second is at 1 position, followed by 2, 3.. space also have position.
#this position number is called as index value.
#position number we always write in []
#get y 
print(a[14])
#get v
print(a[18])

#-----------------------Slicing---------------------------
#Slicing means cutting or chopping or deleting alpahbets from left side or right side
#from left side : 
# syntax : variablename[no of alpahbets we want to delete from left side :]
b="Helloworld"
print(b[3:])

#from right side : 
#syntax  : variablename[: no of alpahbets we want to keep on left side ]
print(b[:7])

#----------------------Reverse strings-------------------------
#variablename[::-1]
c="Coding"
print(c[::-1])

#----------------------Strings Method or functions---------------------
#1. capitalize() : makes first letter of string capital
d="this is good"
print(d.capitalize())

#2. upper() : converts all letters into capital letters
print(d.upper())

#3. lower() : converts all letters into small letters
print(d.lower())

#4. split() : split is used to seperate words in sentence or divide by putting comma in that
e='Johnny shetty'
print(e.split())

#5. len() : to find thw size of string means to count how many total alphabets we have 
f="my name is raha i am 10 years old. i love coding and swimming"
g=len(f)
print(g)

#6. strip() : trim extra space from left or right side.
r="  hello  "
print(r.strip())

#7. find() : it is used to find a specific alpahbet or word if we are looking for
s="this is good"
t=s.find("good")
print(t) # print the index or position of g in string, if that word is not there then nothing is printed on screen.


#--------------------Joining of strings-------------------------
#two ways : 
#using , 
#using + sign 

a1="John sharma"
a3="badminton"
reverse=a1[::-1]
s1=a1.split()
print(a1+" "+"is good"+" "+"my favorite sports is"+ a3)
print(a1,"is good boy", "His favorite sports is", a3, "and when i reverse my nam i get", reverse, 
"after spliting i get", s1
)