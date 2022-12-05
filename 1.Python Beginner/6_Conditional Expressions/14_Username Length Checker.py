'''If a username is lesser than 10 letters it will get accepted otherwise rejected.'''

a = input("Enter your username: ")
b = len(a)

if (b<10):
    print("This username is accepted.")
else:
    print("This username is not accepted.")