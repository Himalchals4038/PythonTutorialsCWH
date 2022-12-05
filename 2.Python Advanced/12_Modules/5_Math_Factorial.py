'''
Factorial operator is same to that in maths. It finds the factorial of the given integer value.
'''

import math

try :
    a = int(input("Enter your desired number: "))
    b = math.factorial(a)
    print(b)
except :
    print("Please enter an integer value only.")