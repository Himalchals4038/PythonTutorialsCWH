num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

a = bool(num1 > num2)
b = bool(num1 == num2)
c = bool(num1 < num2)

print(a & b) # And Operator
print(c & b) # And Operator
print(a | b) # Or Operator
print(c | b) # Or Operator
print(a ^ b) # Xor Operator
print(c ^ b) # Xor Operator