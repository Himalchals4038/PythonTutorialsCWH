# Use open function to access the file.
# Use read function to read the contents of a file.
# Use close access to restrict the file.
# 'r' is used to denote 'readable'.

# f = open('sample.txt', 'r')

f = open('sample.txt')
data = f.read()
print(data)
f.close()

# By default the file access mode is 'r'.