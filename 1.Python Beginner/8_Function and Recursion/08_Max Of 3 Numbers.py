# Program to find the greatest of three numbers input by the user.

def max(a, b, c):
    if (a>b):
        if (a>c):
            return a
        else:
            return c
    else:
        if (b>c):
            return b
        else :
            return c

p = int(input("Enter first number: "))
q = int(input("Enter second number: "))
r = int(input("Enter third number: "))

k = (max(p, q, r))

print("The maximum value is:", k)