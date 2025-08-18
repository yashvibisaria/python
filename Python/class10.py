#------------------------------Functions/methods--------------------------------------------
#Function means to do some work for you.
#There are two types of functions:
#1. Inbuilt functions: which python has created  and we can use them eg : sort(), reverse(), input(), 
#print() etc.. Function always has one word and () with that.
#2. User defined Functions : When user creates his own functions and we can use it. 
#creating function means we are grouping the code together or storing block of lines of code and give a name to it.
#like variables which store only one value but function can store infinifite lines of code
#Reason to create our own function:
#1. if we are looking for a function which is not there then w ehave to create our own function.
#2. as create own function means storing lines of code.  this makes code more orgainzed and readable
#eg : we have a game which has 300 lines of code written like score code, gameover code, player movement,
#enemy  movement, collosion, animation and many more. if we have to serach for gamover code then it will might take lott of time.
#There is another way to do this code. we store all 300 lines of code in differnet functions.
#like w ecreate one gameover function for gamover code, one score function for scoee code, 
#one player function fo all player coding and so on...now if we want to serach for gamover code all we have to do is 
# go insie gameover function. so this makes our code more readable and better to undertand...

#3.Reusing the function : if we ahve 30 lines of code stored in function and we want to use it again we can call the function saving times and making code shorter.
#as we do not have to copy paste.

#with or without functin we get same output.

#syntax for creating function : def functioname():

#Inside we can put any code : list, ddictonary, while loop, for loop, if condition, variables etc...
#syntax to  use or call function : functioname()

#-----------------------------------Non Paramter Function------------------------------------
def even():
    a=int(input("Enter number"))
    if a%2==0:
        print("it is even number")
    else:
        print("it is odd number")

even()
even()
#thi will make code execute twice

#--------------------------------Parameter Functions----------------------------------------------
#Parameter Functions are those functions in which we pass variables in (). the reason for passing variable 
#let say we have code related to a game that we need to store in function. the code is related to player
#movement f player.we will be using same code for  3 different players that menas we will be calling the function 3 times.
#but for small chnages will be there like all players have different shape and size.One option is we can do seperate coding.
#another option is we can so code in function one time and things which are different like color, shape we will not 
#give any color or shape inside the function rather we give it whe we called the function.in this w ecan use sam ecode for all 
#plyares but will few changes when w ecall it.

#Example 1 : create a function marks for different student. Here print there name and marks
def stu(a):
    print(a)
    math=3
    science=4
    total=math+science
    print(a, " has scored", total, "marks")
#when w ecall the function variable is replaced with actual.
#Parameter function is good whne almost all code is same just few values are different then instead of giving actual we give variables
# when later we call ufntcion ew replace variable with actual value

#first student. wherever a is used in code evrytine it replaces it with John after taht priya and then after that riya
stu("John")
stu("priya")
stu("riya")




    