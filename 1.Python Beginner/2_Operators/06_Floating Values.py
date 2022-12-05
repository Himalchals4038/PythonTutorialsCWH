'''Division of any Integer generates a float number whether the number is integer or a decimal.'''

a = 8571
print(type(a))

b = a/3
print(type(b))

# Multiplying a float number with an integer generates a float number only.
# That float number can then be changed to integer by using Typecasting function.

c = b*3
print(type(c))
c = int(c)
print(type(c))