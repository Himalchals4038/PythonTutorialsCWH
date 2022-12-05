# Putting a number n inside the bracket of read makes python print only first n characters of the file. 

f = open('sample.txt')
data = f.read(5) # Only reads first 5 characters from the file.
print(data)
f.close()