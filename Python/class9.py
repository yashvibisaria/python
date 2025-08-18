#------------------------------for loop------------------------------------
#for loop is used to iterate or loop over data structure or where there is lot of data like list, tuple, set, dictonary or range() function.
#its work is to get data from them one by one so that we can use it.

#Reason : if the list is really big like we have 100 of data in it the it is really diffecult to get data manually
#using index value. it is time taking in that case w euse for loop as it will get us the data from list instantly.

#syntax of for loop : for variablename in listname/tuplename/range/dictonary/set:
   #code

#Note : we just need one variable which will go inside the list/tuple/set/dictonary to get data. 
#that is why in keyword is written. as it is variable so it can bring only one data at one time from it.
#so it goes in rounds to bring ine by one all data because it happens repeatdly bringing data so it is called as
#loop. because it does the task of getting data again and again it is called as for loop.

#-------------------------------------Difference between for loop and while loop------------------------
#1. for loop is used to get data from data structure(list etc) in order to use it and while loop is used to repeat the code.

#2. we always need either list/tuple/dictonary or range in for loop but that is the not compulsion in while loop
#it can be it cannot be

#3. both loops can be infinite

#4.break and continue keywords are used bothe loops

#5. we can also created nested loop. nested loop means loop inside loop. eg one for loop and inside that another for loop.
#thsi is possible if we have list inside list
#----------------------------------------range()--------------------------------------------------
#range() is altennate way which w ecan use in case we do not want to reate list and save time.
#but range() work only if numers are in specific order and start and ending. but if that is not there w ecannot use 
#use range() we have to sue list

#Example 1 : without for loop
#get all numbers from list and add them up
list1=[100, 200, 300, 400, 600, 700,800, 900, 1000 ,1200, 1400, 2000000000]
total=list1[0] +list1[1] +list1[2] +list1[3] +list1[4] +list1[5] +list1[6] +list1[7] +list1[8] +list1[9] +list1[10] +list1[11]
print(total)

#with loop
#add all numbers from list
total1=0
for i in list1:
    total1+=i# i is variable hich go isnide and brings data. first it will bring 100 and give to total,
    # then aagain in second round it goes inside and brings 200, total1 already has 100 now it will add 200 +100, s
    #so new value of total1 is 300, now again i goes inside and brings 300. so like this i will keep on brging all number and we add to total1.

print(total1)

#Exampe 2 : use above list abd check for every number if its didviable by 2 then its even else odd

#j brings all data one by one  and w euse if then on all
for j in list1:
    if j%2==0:
        print(j, "is even number")
    else:
        print(j, "is odd number")

#Example 3: print first 10 numbers except 3 and 8.
for m in range(1,11):
    if m==3 or m==8:
        continue
    print(m)

#last number in range is not included
#library are the inbuilt python files where we have inbuilt functions which can be used into our code. In order to use any functions from the
#library, we have to first connect with the library by importing it at the top. We have different libraries for different things like games, websites etc.
#Random is a library which has different types of random functions 
#Libraries are created later on after developing the language by different people in order to make code quicker. That is why in order to use the
#functions from them we have to import them.
import random

#randint generates a random number between a specific range 
a=random.randint(1,10)
print(a)

#---------------------------------------Assignment-----------------------------------------
#create a list of fruits. use for loop and print all fruits
#use range()  of even numbers betwee 2 to 60. use for loop. check if numbera divisble by 2 then print it is even number
#else print it is odd number.

list2=["grapes","apple","banana","oranges","beetroot"]
for k in list2:
    print(k)


for l in range(2,60):
    if l%2==0:
        print(l, "is an even number.")
    else:
        print(l, "is an odd number.")