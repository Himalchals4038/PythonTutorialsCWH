'''
Absolute function is equivalent to modulus operator of maths.
It changes negative values to positive and leaves the positive values unaltered.
'''
import math
try:
    a = float(input("Enter your desired number: "))

    b = math.fabs(a)
    print(b)
except:
    print("Please enter a number only !!")
