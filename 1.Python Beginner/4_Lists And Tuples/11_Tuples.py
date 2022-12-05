t = (15, 36, 29, 94, 56, 79)
print(t)
print(t[0])
print(t[1])
print(t[2])
# Tuple works exactly like list when printing the whole or a part of the tuple.

# But tuple doesn't allow us to change data like list.
# t[2] = 62 will show error as data change is not accepted in tuple.

t1 = ()
print(t1)
# Here t1 is called an empty tuple.

t2 = (1) 
print(t2)
# Here python will not recognise it as a tuple and will detect it as a string.

t3 = (1,)
print(t3)
# Here python will recognise it as a singular tuple.

