L1 = [264, 316, 193, 471, 619, 943]
L1.insert(0, 26)
print(L1)
L1.insert(5, 49)
print(L1)
L1.insert(-3, 163)
print(L1)

# insert function is used to add required value inside the list.
# in brackets we first write the index where it is to be inserted and then the value to be inserted.
# when we use -ve sign to insert values we must remember that the value will come in the list after the index it has been denoted. 
# For eg. if we want to add 45 at -6 index, we have to write (-5, 45).