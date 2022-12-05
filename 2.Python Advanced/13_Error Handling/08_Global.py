'''Global Variable is used for all functions in the file except 
if a specific part of that program has a local value assigned to it.'''

a = 54 # Global Variable
def func1() :
    a = 8 # Local Variable
    print(a)
func1()
print(a)

'''Value of global variable can be changed using global function.'''

b = 5 # Global Variable
def func1() :
    global b
    print(f"Value of b is: {b}")
    b = 16 # Local Variable turned into global variable by the global command. 
    print(f"Value of b is: {b}")
func1()
print(f"Value of b is: {b}")