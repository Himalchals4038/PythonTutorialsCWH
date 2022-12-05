'''In slicing each letter of string is given a number based on their position. Here the numbering starts from zero instead of one.'''
# For eg. in "Rock" R=0 o=1 c=2 k=3 
# Or in reverse order k=-1 c=-2 o=-3 R=-4

name = "Dickens"
print(name[0])
print(name[1])
print(name[2])
print(name[3])

# print(name[7]) will show error as no value is assigned to number 5 in the string.
# name[3] = d --> Does not work.

print(name[0:6]) 
# This will print the first 6 letters of name and the seventh one assigned to number 6 will be left out.
print(name[1:5])
# This will print the 4 letters from i to e and leave out the rest.
print(name[0:])
# This will print the whole letter starting from D. So it is same as print(name[0:7])
print(name[:6]) 
# This will print the whole word except s. So it is same as print(name[0:6])
print(name[-6:-2])
# This is same as print(name[1:5])