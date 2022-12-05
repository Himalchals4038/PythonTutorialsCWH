'''Write function allows us to create and edit a file.'''

f = open('second sample.txt', 'w')
f.write("This is the second file wich is being generated directly from python using edit function.")
f.close()

f = open('second sample.txt', 'w')
f.write("This is the second2 file wich is being generated directly from python using edit function.")
f.close()
# # This command edits the previous file and adds 2 after second in file.

f = open('second sample.txt', 'a')
f.write(" Adding in a few more Lines.")
f.close()
# Append adds the given line to the txt file without altering the previous one.

f = open('second sample.txt', 'w')
f.write("Removing all the other files and starting a new one.")
f.close()
# This command will erase any other text in the file and start with a new one.