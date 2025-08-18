#----------------------------While loop------------------------------------------
#whenver our code is repeating in order to save time and make code shorter we can use while loop.
#while loop will repeat the code without writing it again and again.
#4 imp things in we need to give in while loop:
#1. start point or when the loop will begin. create variable and store start value in that.
#2. when the loop will end ir how many times we need to repeat
#3. code to repeat  or task that need to repeat
#4. increament or decreament for code to keep on going (counting)

#w=if we tell someone that they need to repeat something again n again 4 things they will ask:
#1. what is the thing that needs to repeat
#2. how many times we need to repeat
#3. when to start
#4. counting

#These 4 things are same as what we do in while loop in coding.

#syntax for while loop :
#variable=startpoint
#while varibalename<=10:
#  code to repeat
#  increament

#-------------------------------------------Benefits-------------------------
#1. saves time
#2. makes code shorter

#Example : print hello 20 times
#Method 1 without loop:
print("hello")
print("hello")
print("hello")
print("hello")
print("hello")
print("hello")
print("hello")
print("hello")
print("hello")
print("hello")
print("hello")
print("hello")
print("hello")
print("hello")
print("hello")
print("hello")
print("hello")
print("hello")
print("hello")
print("hello")
print("hello")
print("hello")
print("hello")

#Method 2 :  while loop
#start value
a=1
#end
while a<=20:# whne a will becomes 21 thne loop stops. condition is till the time a is less than 20 loop goes on.
#whne opposite of this condition happens that a becomes gretare than 20 loop stops.
    #tell what code to repeat
    print("hello")
    a+=1 # increament is done because a right now is  but our loop stops when a is >20. so in order to make a 20 we have to
    #increament by 1 so it reaches 21

#Example 2 : print all odd numbers from 1 to 30
b=1
while b<=30:
    print(b)
    b+=2

#Example 3 : print square of every number from 1 to 10

c=1
while c<=10:
    print(c*c)
    c+=1

d=1
fact=1
while d<=25:
    fact*=d
    d+=1

print(fact)

#Between 1 to 12, check which ones are the even numbers and which are the odd numbers. Print them.

e=1
while e<=11:
    e+=1
    if e% 2 ==0:
        print(e, "is an even number.")
    else: 
        print(e, "is an odd number.")

#Infinite loop example. In this, the loop keeps on going and never stops. So, in a condition, we don't write when it will stop instead we right true.

f=1
while True:
    print("hello")
    if f==30:
        break
    f+=1


# Break and continue keywords
# Break is used when we want to stop the infinite loop at any point of time. 
# Continue is used when we want to stop the loop at one point but again want it to restart afterwords, then continue afterwords.

# Print first ten numbers, skip three and seven.

g=1
while g<=9:
    g+=1
    if g==3 or g==7:
        continue
    print(g)