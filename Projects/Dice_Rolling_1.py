
b = str(input("Do you want to start rolling ??\n"))

if b == 'y' :

    while (True):
        import random
        a = random.randint(1,6)

        print("Dice Rolling...")
        print(f"The output is {a}")

        c = str(input("Do you want to continue rolling ??\n"))

        if c == 'y' :
            pass
        else :
            print("Ok no problem.")
            break
else :
    print("Ok no problem.")
