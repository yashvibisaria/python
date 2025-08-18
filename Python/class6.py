#-------------------------------Operators----------------------------
#1. Arthimetic : +, -, *, /, %(modulus)
#2. Comparison :<, >, <=, >=, ==(equal)(as = is used to assign value in variable). == ussed only on condition., !=(not equal)
#3. Assignment : this is used to assign/ give  value to variable using +, -, *, / eg : 
a=3
a+=3 # we are adding 3 to a. a is already having 3 . now enw e add 3 to ad it becomes 3+3 which is 6
print(a) # 6
#eg 2 : if we have score=0, and when player wins in game we give 10 score to it becoms score+=10, 
#similary we can decraesebas well using score-=10
#4. Logical : or(either of two condition), and(both two conditions), not(no condition)

#---------------------------Conditions--------------------------------------
#if one condition gets executed then another thing happens
#syntax
#if condition:
#  next 
#elif condition:
#  next
#else:
#  next

#Example 1:  take input from us. check if it is above 18 then print it is above 18 else print less than 18
number= int(input("Enter number"))
if number>=18:
    print("it is above or equal to 18")
else:
    print("less than 18")

#Example 2 : take input form user  subject  and score. if subject is equal to math and score is between 90 to 100 then print
#you have score grade A in math elif  subject is equal to science and score is between 90 to 100 then print
#you have score grade B in science else print you score nothing in any subject 

subject=input("Enter subject")
score=int(input("Enter your score"))
if subject=="math" and (score <=100 and score>=90):
    print("you have scored grade A in math")
elif subject=="science" and (score <= 100 and score>=90):
    print("you have scored grade B in science")
else:
    print("you have scored nothing in any subject")


#first Python code
print('Hello')

#variable myname
myName="Neha"

#printit
print (myName)
#check data type
type(myName)

#find length of name
print(len(myName))





