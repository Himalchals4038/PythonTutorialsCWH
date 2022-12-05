'''We can 'try' to change one type of data to another. Only pure integers, both +ve and -ve, can be changed from one from to another i.e. numnerical, float, string.'''

a = "-145"
print(a)
print(type(a))

# Initially the data type is string.

a = int(a)
print(a)
print(type(a))

# Now the data changes to integer.

a=float(a)
print(a)
print(type(a))

# Finally the data changes into float numbers.