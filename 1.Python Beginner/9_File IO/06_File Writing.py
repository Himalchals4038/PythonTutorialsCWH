'''If a file is open and we write multiple things with separate commands, all will be displayed.
   Also use \n to put all the sentences in different else all will br printed in same line without a gap between 2 sentences.'''

f = open('third sample.txt', 'w')
f.write('Ok so this is the third file.\n')
f.write('I will be writing a few things in it.\n')
f.write('Hope it displays all the things properly.\n')
f.write('Wow its actually working properly !!')
f.close()