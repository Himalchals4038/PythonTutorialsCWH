'''
Ceiling is a math operator which returns the smallest integer value more than or equal to the given number.
Written as math.ceil() and we need to import math library to use it.

If we input 16.3 we get 17 as output.
If we input -16.3 we get -16 as output.
If we input 53 we get 53 as output.
If we input -53 we get -53 as output.
'''
import math

a = float(input("Enter your desired number: "))

b = math.ceil(a)
print(b)