a = 28
b = 23

print(a, bin(a))
print(b, bin(b))

print(a&b, bin(a&b))
print(a|b, bin(a|b))
print(a^b, bin(a^b))

print((15 & 2), bin(15 & 2))
print((69 & 90), bin(69 & 90))
print((79 & 32), bin(79 & 32))

# & 'and' operator works with the binary value of the corresponding integers input values.
# & operator changes both of the given numbers to binary and runs & operator on individual unit places.
# Same is the case with | 'or' and ^ 'xor' operators. 
# After running the operators on both numbers it reverse changes binary to integer and displays result as output.