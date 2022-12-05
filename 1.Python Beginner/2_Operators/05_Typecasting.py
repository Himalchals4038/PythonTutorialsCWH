'''Typecasting is the changing of one form of data to other using int str float functions.'''

# a = "97856"
# print(a+34)
# Error will be displayed at output as a is a string variable here whereas 34 is a numerical value.
# Two different types of quantities can't be added together.

a = "2648"
print(type(a))
a = int(a)
print(type(a))
print(a+45)

# Int function 'tries' to change the type of data to integer. Not all data can be changed eg.Madan567 can't be changed to integer.
# Two values of same type can be made to interact.

b = 6804
print(type(b))
b = str(b)
print(type(b))
b = float(b)
print(type(b))

# "47" is a string literal whereas 47 is a numeric literal.