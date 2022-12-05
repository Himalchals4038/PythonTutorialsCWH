'''If a value satisfies more than one conditionals the first conditional wil be accepted and accordingly specific functions will be carried out.'''

b = input("Enter the value of b: ")
b = int(b)
if (b>=0) :
    print("b is a positive number.")
elif (b<=0) :
    print("b is a negative number.")
else :
    print("b is zero.")


c = input("Enter the value of c: ")
c = int(c)
if (c<=0) :
    print("c is a negative number.")
elif (c>=0) :
    print("c is a positive number.")
else :
    print("c is zero.")