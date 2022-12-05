z = str(input("Do you want to start rolling ??\n"))

if z == 'y' :
    while (True):
        import random

        a = random.randint(1,6)
        b = random.randint(1,6)
        
        if a == b :
            print("Both outcomes are equal.")
        else :
            print("Both outcomes are not equal.")
        
        c = str(input("Do you want to continue rolling ??\n"))

        if c == 'y' :
            pass
        else :
            print("Ok no problem.")
            break
else :
    print("Ok no problem.")
