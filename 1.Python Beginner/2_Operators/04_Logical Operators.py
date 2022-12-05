# Logical Operators are and or not nand nor xor etc.

from operator import truediv


bool1 = True
bool2 = False

print("The value of bool1 and bool2 is", (bool1 and bool2))
print("The value of bool1 or bool2 is", (bool1 or bool2))
print("The value of not bool1 is", (not bool1))
print("The value of not bool2 is", (not bool2))
print("The value of not bool1 and bool2 is", (not (bool1 and bool2)))
print("The value of not bool1 or bool2 is", (not (bool1 or bool2)))
