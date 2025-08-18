
while True:
    a=int(input("Enter the first number"))
    b=input("Enter the operation +,-,*,/")
    c=int(input("Enter your second number"))
    if b=="+":
      print(a+c)
    elif b=="-":
      print(a-c)
    elif b=="*":
      print(a*c)
    elif b=="/":
      print(a/c)
    else: 
      print("Invalid")
    choice=input("Do you want to coninue? Yes/No")
    if choice=="Yes":
      continue
    else:
      print("Thanks for using the app")
      break
