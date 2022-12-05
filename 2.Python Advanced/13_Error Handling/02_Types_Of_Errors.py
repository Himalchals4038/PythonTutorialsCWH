'''

They are different types of errors in Python. Some of them are as follows:
a = 52/0  --> This will show Zero division error
a = int(653adcb)  --> This will show Syntax error
a = int(flsj)  --> This will show Name Error
a = '2' + 2 --> This will show Type Error

a = int('utof') --> This will show Value Error
l = [15, 77, 3, 0.56] print(l[4]) --> This will show index out of range error.

d = {
    'Python' : 'Easy to use and versatile'
    'JavaScript' : 'Much tougher and used in almost every field'
    'C++' : 'Even tougher than JS and used in Gaming Industry'
}
print(d['Ruby']) --> This will show key error as Ruby is not present as key in the dictionary.

import operators --> This will show ModuleNotFound error as there is no module named as 'operators' in-built in Python.
Also we have not made any file named as 'operators.py' in our folder.

from cal import Sum1
print(Sum1(10, 5)) --> This will return import error as there is no function named as Sum1 in cal.py 

'''
from cal import sum
print(sum(15, 26))
