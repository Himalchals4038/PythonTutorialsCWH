square = lambda a : a*a

l = [16, 90, 33, 41, 58]
# m = []

# for item in l :
#     z = item**2
#     m.append(z)
# print(m)

print(list(map(square, l)))

# Mapping is a shorter way to alter the elements of a list.
# Map is a function which applies to all the items in the input list.