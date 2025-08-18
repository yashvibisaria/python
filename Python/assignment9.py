# Create a dice game. create a function dice . Inside that Generate a random number, (1,6), if the number comes out to be 6, print You win, and else you lose.

def dice():
    import random
    a=random.randint(1,6)
    print(a)
    if a==6:
        print("You win!")
    else:
        print("You lose!")

dice()