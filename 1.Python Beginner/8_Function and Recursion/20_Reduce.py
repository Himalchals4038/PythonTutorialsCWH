from functools import reduce

sum = lambda a,b : a+b
mul = lambda c,d : c*d

l = [56, 25, 48, 0.5, 1.28]

z = reduce(sum, l)
print(z)

y = reduce(mul, l)
print(y)

'''
Lambda Function takes elements of the list sequentially and 
replaces them with the result of the process defined by the user.
In z it takes 56 and 25 at a time and replaces them with 81, 
after that it takes 81 and 48 at a time and replaces them with 129.
'''


