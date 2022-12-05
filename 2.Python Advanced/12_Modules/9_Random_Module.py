'''
Random is a module in python which generates random value based on restrictions set by the coder.
'''

import random

print(random.randint(2, 10))
# Both 2 and 10 are included here.

print(random.randrange(15, 50))
# 15 is included but 50 isn't included.

a = ['python', 'java', 'javascript', 'c++', 'ruby', 'swift']
print(random.choice(a))
#  A random string is chosen among all the strings.

print(random.random())
# Random function returns a random float number between 0 and 1.

b = ['python', 'java', 'javascript', 'c++', 'ruby', 'swift']
random.shuffle(b)
print(b)
# Shuffle changes the order of the values inside a list in a random order.

print(random.uniform(12, 50))
# Uniform function generates a random float value between the numbers.