# Alteration of previous question using def function.

def factorial_iter(a):
    p = 1
    for i in range (a):
        p = p * (i+1)
        i = i + 1
    return p

a = int(input("Enter the number you want to find factorial of: "))

f = (factorial_iter(a))

print(f)