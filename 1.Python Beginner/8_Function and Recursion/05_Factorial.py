# Program to find factorial of a given number.

a = int(input("Enter the number you want to find factorial of: "))
p = 1

for i in range (a):
    p = p * (i+1)
    i = i + 1

print("Factorial of given number is :", p)