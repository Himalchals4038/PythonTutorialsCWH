'''Write a program to rename an existing file in folder.'''

import os

oldname = 'fifth sample.txt'
newname = 'fifth_renamed.txt'

with open(oldname) as f :
    content = f.read()

with open(newname, 'w') as f :
    f.write(content)

os.remove(oldname)