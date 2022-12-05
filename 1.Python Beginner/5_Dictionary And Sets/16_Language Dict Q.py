'''First create and empty Dictionary.
Take input the favourite language of your 4 friends and then update them into the empty Dictionary.
Then diplay your friend's name followed by his/her favourite language.'''

a = {}

F1 = input("Enter favourite language of Sam: ")
F2 = input("Enter favourite language of Tom: ")
F3 = input("Enter favourite language of Dick: ")
F4 = input("Enter favourite language of Harry: ")

b = {
    "Sam": F1,
    "Tom": F2,
    "Dick": F3, 
    "Harry": F4
}

a.update(b)

print(a)