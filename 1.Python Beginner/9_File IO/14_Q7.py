'''Find whether a value is present in a file and is present, specify the line and line number.'''

content = True
i = 1

a = str(input("Enter the word to be found: "))

with open("log.txt") as f :
    while content :

        content = f.readline().lower()

        if 'python' in content.lower() :
            print(content)
            print(a, f"is present in the file on line number {i}.")
            print(i)
        i = i + 1 # or you can use i+=1 