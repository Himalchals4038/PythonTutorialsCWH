def readFile (filename) :
    try :
        with open (filename, 'r') as f :
            print(f.read())
    except FileNotFoundError :
        print(f"File {filename} is not found.")

readFile('1.txt')
readFile('11.txt')
readFile('2.txt')
readFile('3.txt')
readFile('9.txt')