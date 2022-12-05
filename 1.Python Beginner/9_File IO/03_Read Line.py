'''Readline reads a particular line of the file starting from first one and consecutively going down.'''

f = open('sample.txt')

# Reads first line. 
data = f.readline()
print(data)

# Reads second line.
data = f.readline()
print(data)

# Reads third line.
data = f.readline()
print(data)

# Reads fourth line and so on.
data = f.readline()
print(data)

f.close()