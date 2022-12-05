from functools import reduce

'''
Write a program to separate the numbers from a list which are divisible by 5.
Use Filter function to separate out the satisfying numbers.
'''

l = [16, 30, 85, 66, 90, 15]

func = lambda a : a%5 == 0
print(list(filter(func, l)))

z = reduce(max, l)
print(z)

