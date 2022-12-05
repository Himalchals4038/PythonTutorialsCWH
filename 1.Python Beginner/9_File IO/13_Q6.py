'''Write a program to detect if a word is present in a specific file irrespective of case.'''

a = str(input("Enter the word to be found: "))

with open("log.txt") as f :
    content = f.read().lower()

if a in content :
    print(a, "is present in the file.")
else :
    print(a, "is not present in the file.")

# lower() changes all the case of the text to lower.