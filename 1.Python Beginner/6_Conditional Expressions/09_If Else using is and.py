from operator import truediv


a = int(input("Enter result of first terminal: "))
b = int(input("Enter result of second terminal: "))

a = bool(a)
b = bool(b)

if (a is True and b is False):
    print("First Gate")
elif (a is False and b is True):
    print("Second Gate")
elif (a is True and b is True):
    print("Third Gate")
else: 
    print("Not Allowed")