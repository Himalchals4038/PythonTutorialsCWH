'''Check if the person's name is there on the list of candidates or not.'''

Names = ['Manish', 'Rohan', 'Soham', 'Vignesh', 'Suraj', 'Diksha', 'Hari', 'Manoj', 'Dinesh']

UserName = input("Enter your name: ")

if (UserName in Names):
    print("You name is there on the list.")
else:
    print("Your name is not there on the list.")