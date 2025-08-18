def dice():
    import random
    a=random.randint(1,6)
    print(a)
    if a==6:
        print("You win!")
        b=random.randint(1,6)
        print(b)
        if b == 6:
            print("You win!")
            c=random.randint(1,6)
            print(c)
            if c==6:
                print("You lose all three!")
            else: 
                print("You lose!")
        else:
            print("You lose!")

    else:
        print("You lose!")

dice()