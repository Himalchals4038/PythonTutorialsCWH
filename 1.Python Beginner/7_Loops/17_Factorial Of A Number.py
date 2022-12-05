from re import I


'''Write a program to find factorial of number given by user.'''

a = int(input("Enter your desired number: "))

p = 1

for i in range (1,a+1):
    p = p*i

print("Factorial of given number: ", p)