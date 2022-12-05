a = int(input("Enter your desired number: "))

if (a>=40):
    if (a==40):
        print("a is equal to 40")
    else:
        print("a is greater than 40.")
elif (20<=a<40):
    if (a==20):
        print("a is equal to 20")
    else: 
        print("a is greater than 20 and lesser than 40.")
elif (0<=a<20):
    if (a==0):
        print("a is equal to 0")
    else:
        print("a is greater than 0 and lesser than 20.")
elif (-20<=a<0):
    if (a==-20):
        print("a is equal to -20")
    else:
        print("a is between -20 and 0")
else: 
    print("a is lesser than -20.")