'''
Pickle is a module used for pickling data. It accepts data and file object. 
The dump() function then serializes the data and writes ot to the file.
Pickle stores the data in the file in binary format.
'''
#Syntax:  dump(obj,file)

import pickle

l = [3, 8, 6, 0, 18, 26]
file = open('writedata.txt', 'wb') # wb stands for write binary
pickle.dump(l, file)
file.close()