team=input("Enter your team.")
code=int(input("Enter the code"))
if team=="A" and code==1999:
    print("There is a traitor in Team B. Find him without letting team know because it can be anyone.")
elif team=="B" and code==2422:
    print("The president is in danger. Keep a watch over him secretly.")
elif team =="C" and code==1832:
    print("There is a traitor in team A. He is off guard for now because of wrong information. This is the best chance to catch him.")
elif team=="D" and code==3943:
    print("Assasinate the minister.")
else:
    print("Intruder alert!")