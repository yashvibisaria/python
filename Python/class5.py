# Dictionary
# is also used to store data but dictionary stores two things, it stores data and keys
# Keys here means the the meaning of the data
# That is how it is different from lists, which stores only data
# This dictionary is similiar to the real life dictionary
# Dictionary has a word and the meaning of the word.
# Similiarly, this dictionary has a data/value and the meaning of it.
#{} is used to create dictonary.

#syntax to create dictonary :
#dictonaryname={"keyname":value, "keyname":value,................}
list1=[100, 200, 'Yashvi', 'a@gmail.com']
dict1={
    'eng_marks': 100,
    'math_marks':200,
    'Name':"Yashvi",
    'email':"a@gmail.com"
}
print(dict1)

#----------------------Access only one data/value---------------------------
#use keyname
#get yashvi
print(dict1["Name"])


#Functions in Dictonary
#1. values() : all values
print(dict1.values())

#keys() : all keys
print(dict1.keys())

#---------------Replace values in dictonary
dict1["Name"]="John"
print(dict1)

#-------------------Add data in Dictonary
dict1["age"]=12
print(dict1)

#------------------delete data from dictonary--------------
dict1["Name"]=""
print(dict1)

#--------------------Example------------
d={"name":[23, 456, 67]}
#we need to solve every bracket. like if [] then write index value nad if {} comes write keyname.
#67
print(d["name"][2])

d={"name":"John", "marks":[12, 23, 45, 78, {"age":[12, 23, 78, 90]}]}
#get 90
print(d['marks'][4]['age'][3])

#Dictonary and list and mutable means we can change it
#----------------------------------Tuple-------------------------------
#Tuple is similar to list where w ecan only store values but its little different from list. once tuple is created we cannot 
#add or delete any data from it. liek in list we have append() and pop() to add or delete. tuple is fixed.() is used fto created tuple.
#Use tuple only when we are sure that we will never add or delete any data from it.
#syntax for tuple : (data1, data2....)
# tuple is immutable that means w ecannot change it
#unlimited data w ecan store. index value is also there in tuple
tp=(23, 12, 100, 200, "hello")
print(tp)
print(tp[3])


