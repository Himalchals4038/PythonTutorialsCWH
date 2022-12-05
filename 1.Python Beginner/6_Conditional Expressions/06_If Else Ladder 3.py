z = input("Enter the desired value of z: ")
z = int(z)

if (z>50):
    print(1)
elif (z>40):
    print(2)
elif (z>30):
    print(3)
elif (z>20):
    print(4)
elif (z>10):
    print(5)
else: 
    print(6)

'''Here the first condition gets satisfied so python doesn't move to next conditions and thus 1 is displayed as output.'''
# In If-Elif_Else ladder python moves from one ladder to next i.e it checks one condition and then moves to next.
# If the value satisfies any condition in between, python stops right there and carries out associated functions.
# If none satifies the value, python executes the else function.