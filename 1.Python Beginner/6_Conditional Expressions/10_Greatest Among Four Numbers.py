# Input different numbers and show which one is the greatest among them.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if (a>b and a>c and a>d):
    print("First number is greatest.")
elif (b>a and b>c and b>d):
    print("Second number is greatest.")
elif (c>a and c>b and c>d):
    print("Third number is greatest.")
elif (d>a and d>b and d>c):
    print("Fourth number is greatest.")
else:
    print("Error in inputing numbers.")