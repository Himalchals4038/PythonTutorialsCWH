'''Random is a function which displays a random value out of the given values.'''

import random
# Random needs to be imported each time when using it.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

randomNo = random.randint(a, b)

print(randomNo)