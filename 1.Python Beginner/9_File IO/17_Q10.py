'''Write a program to delete the contents of a previously made file.'''

with open('fourth sample.txt') as f :
    f1 = f.read()
    print(f1)

with open('fourth sample.txt', 'w') as f :
    f2 = f.write("Everything has been deleted !!")
    
with open('fourth sample.txt') as f :
    f3 = f.read()
    print(f3)