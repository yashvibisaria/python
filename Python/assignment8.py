a=input("Enter the word.")
b=a[::-1]
print(b)
list1=[]

while True:
    password=input("Enter your password.")
    if password == "Yashvi":
        print(password)
        break
    else: 
        list1.append(password)
        print(list1)
        continue