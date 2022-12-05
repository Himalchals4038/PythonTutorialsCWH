'''Write a program to find whether a number is prime or not.'''

i = int(input("Enter your desired number: "))
i = abs(i)

p = 0
s = 0

if (i != 2):
    for j in range (2, i):
        s = i%j
        if (s==0):
            p = p + j
        else:
            pass
    if (p == 0):
        print("The number is prime.")
    elif (p != 0):
        print("The number is not prime.")
    else:
        print("Neither prime nor composite.")    
else:
    print("The number is prime.")



        