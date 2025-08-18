#------------------------------Different libraries---------------------------------------
#time library :time functions

import time

#sleep() : It is used ti make program wait to execute for seconds, minutes
#Example : print numbers 1 to 11 with  wait of 3 seconds

#a=1
#while a<=11:
 #   print(a)
  #  a+=1
   # time.sleep(3)

# Date time library. It has the functions related to date and time. 
# Now is used to get the current date and time.
import datetime
a=datetime.datetime.now()
print(a)

#STRFT is used to get or extract different forms of time in abbreviation forms.
# Example, if we want to know only weekday, we have to write down S inside the function then it will extract the weekday from the current time.
print(a.strftime("%B"))
print(a.strftime("%A"))
print(a.strftime("%W"))
print(a.strftime("%D"))
print(a.strftime("%m"))
print(a.strftime("%Y"))
print(a.strftime("%H")) # 24hr
print(a.strftime("%I")) # 12hr
print(a.strftime("%m"))
print(a.strftime("%p"))
print(a.strftime("%w"))

#Calender library: the calender, it has a lot of functions related to calender
import calendar
print(calendar.month(2025, 6))
print(calendar.calendar(2026))
print(calendar.isleap(2022))
print(calendar.weekday(2025,6,4))

#Math library : math library has math functions
import math
print(math.ceil(3.4)) #Gives smallest integer greater than the value in the round bracket
print(math.floor(4.5)) # Returns greatest integer less than 4.5
print(math.fabs(4.7)) # Absolute value
print(math.factorial(5)) # factorial means multiplying given number with previous number till one (5x4x3x2x1 i sfactorial of 5)
print(math.gcd(3, 6)) # This is used to found out the greatest common diviser
print(math.pow(4,2)) #Pow means power
print(math.sqrt(49)) #finds square root
print(math.exp(3)) # exponent
# We have different trigonometry functions like sin, cos, tan etc..

# There is a pi function that gives the value 3.14.

# Collections functions are used to count. Counter is used to count the numbver of times anything is coming in a list, tuple, string
import collections
list1=[1,2,3,30,30,1,50]
print(collections.Counter(list1))


