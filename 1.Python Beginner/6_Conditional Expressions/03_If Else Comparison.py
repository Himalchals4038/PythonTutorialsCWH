'''Program to compare which one of the two given numbers is greater or smaller.'''

a = input("Enter First number: ")
b = input("Enter Second number: ")
a = int(a)
b = int(b)

if (a>b): 
    print("First is greater than Second.")
elif (a<b):
    print("First is lesser than Second.")
else : 
    print("First is equal to Second.")