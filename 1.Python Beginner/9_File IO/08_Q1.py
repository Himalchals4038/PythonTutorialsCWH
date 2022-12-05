'''Program to read a given file and find whether a specific word is present in it or not.'''

f = open('blind typing.txt')
t = f.read()

w = str(input("Enter the word to find: "))

if w in t :
    print('The word is present in file.')
else :
    print("The word is not present in file.")

f.close()