def greet(name) :
    print(f"Good Morning, {name}")

def age(age) :
    print(f"Your age is {age}")

print(__name__)
# Above command displays __main__ when executed in this file and 
# displys the name of this file when used as import in another file.

if __name__ == "__main__" :
    a = str(input("Enter your name: "))
    greet(a)

if __name__ == "__main__" :
    b = int(input("Enter your age: "))
    age(b)


# __name__ == "__main__" evaluates the name of the module from where the python program is ran.