'''With statement is a easier way to tackle with files as we don't need to close the file at end. It closes automatically.'''

with open('third sample.txt', 'r') as f :
    a = f.read()
print(a)

# Reads the third sample and prints it as output.

with open('third sample.txt', 'w') as f :
    b = f.write('Deleted Everyting !!')
print(b)

# Removes all previous data from file and prints the sentence given in bracket.
