'''Input function is used to put your desired data during the execution of the command. All the data in Input function is string type.'''

# a = ("Type your desired number: ")
# print("The output is: ", a**3)

'''Here the command can't be executed as a is a string whereas is an integer so at first we have changed that string value to integer.'''

a = input("Type your name: ")
b = input("Type your age: ")
b = int(b)
c = 2022-b

print("Your name is: ",a)
print("Your birth year is: ",c)
print("Your age is",b,"years old.")
print(f"Your age is {b} years old.")
