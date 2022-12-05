# a = 25
# b = 36.45
# c = 2 + 6j

# print("The type of variable that a is:",type(a))
# print("The type of variable that b is:",type(b))
# print("The type of variable that c is:",type(c))

# For complex numbers python changes i to j. 
# 2+6i has to be written as 2+6j for python to detect it as complex numbers.

d = eval(input("Enter first value: "))
e = eval(input("Enter second value: "))
print(d + e)

# eval itself determines the type of data input by user and accordingly follows the process.
# eval accepts integer, float, complex, binary, etc.