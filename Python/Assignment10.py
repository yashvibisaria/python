#create a function hello. Inside that tke inputs from user usernam and password. check if they are equal to specific username and password
#print its correct else print its incorrect. it will keep on asking the user to enter correct username and password
#unless correct one in entered . use while loop, break, continue

def hello():
    while True:
        username=input("What is your username?")
        password=int(input("What is your password?"))
        if username=="Yashvi" and password==2810:
            print("It is correct.")
            break
        else:
            print("It is incorrect.")
            continue
hello()
#Exampel 2 : chekc if nume is perfect square in function
#perfect square means if the number whcih is ther has come after multiple of same numer with each other tehn it is perfect square
#36 is perfect square as 6x6. 100 is perdect square 10x10. 20 is not perfect square 4x5

#inbuilt function which calculates sqrt() square root of number means perect square kind of. 
import math
def square():
    a=int(input("What is your number?"))
    rs=math.isqrt(a)
    #this will find out sqrt of every number. eg : sqrt of 25 is 5, 100 is 10.. 20 will in decimal.
    # if decimal comes that means that number is not perfect square. it should be integer the sqrt
    #is_integer() check if given no is interger or not
    if rs*rs==a:
        print("it is perfect square")
    else:
        print("it is not a perfect square")


square()

#Example take input from user and check if the number is bothe perdect square and even number then print they 
#are perect square and even number else they are not


def even():
    b=int(input("What is your number?"))
    rs2=math.isqrt(b)
    if rs2*rs2==b and b%2==0:
        print("It is a perfect square and even number.")
    else:
        print("It is not a perfect square or it is an odd number.")

even()

#Example 5 : take input from user. reverse the input. check if two variables are equal then it is palindrom else it is not a 
#palindrom

def palindrome():
    word=input("Enter the word.")
    if word[::-1]==word:
        print("It is a palindrome.")
    else:
        print("It is not a palindrome")

palindrome()

#-------------------------------Assignment-----------------------------------------
#resvise all topics, ask if any doubts. will take a small test
# 