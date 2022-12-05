'''Write a program to accept a sentence from the user and change all is to was. Also strip it of unnecessary spaces.'''

def remove_and_strip(string, word):
    newStr = string.replace(word, "was")
    return newStr.strip()

a = str(input("Enter your sentence: "))

b = remove_and_strip(a, "is")
print("The filtered word is: ", b)