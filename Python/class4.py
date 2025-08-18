#-------------------------List-----------------------------------------------
#List allows us to store lot of data altogether. inside one list  ecan store any data like nmbers, integers, 
#float, boolean value, strings etc..[] is used to create a list. we can store unlimited  there is no limit
#syntax for creating list : listname=[data1, data2, data3, data4...........]
list1=[1, 2, 3, "hello", True]
print(list1)

#-------------------Index value---------------------------------------
#Index value is position number given to every data which starts from 0, 1, 2... so on....
#Reason for assiginning index value:
#if we want to get any specific data from list thne w ecan use this
#syntax to True
#get hello

print(list1[3])

# get True
print(list1[4])

#--------------------------List functions----------------------------------
#1. append() :it is used to add the data in list later. 
list1.append("Akshi")
print(list1)

#2. pop() : it is used to delete data from list. automaticaly whatvere is at the end will be deleted.
list1.pop()
print(list1)

#3. sort() : sort is used to sort list in number order or alphabetically.
#list should have only alphabets or only numbers
list2=[12, 100, 30, 60, 1,  19, 200, 1000, 23]
list2.sort()
print(list2)

#4. reverse(): reverse the list
list2.reverse()
print(list2)

#5. len : used to fins the size of data in list
l=len(list2)
print(l)

#6 insert() : is used to add adata list st specific position
list2.insert(2, "orange")
print(list2)
#)7 remove() used to delete any data from list
list2.remove(100)
print(list2)

#8. count : countsthe number of data repeating
list2.count(1000)
print(list2)

#---------------------------Nestining of list----------------------------
# this mean creating list and inside that another l
a=[[1, 2, 3, 4  ] ]                 
b=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c=["hello", " this is good"]
print(b+c)

# slicing means deleting from the left side and from the right side
# list 
print(list1[2:])
