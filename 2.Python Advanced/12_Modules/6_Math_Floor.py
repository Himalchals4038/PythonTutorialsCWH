'''
Floor function works exactly like box function and returns 
the greatest integer value less than or equal to the given number.
'''
import math

try:
    a = float(input("Enter your desired number: "))
    b = math.floor(a)
    print(b)
except:
    print("Please input number only.")