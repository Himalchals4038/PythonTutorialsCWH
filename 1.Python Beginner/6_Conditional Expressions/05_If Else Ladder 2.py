'''In If-If-Else ladder python checks all if conditionals at once and if none satisfies the value it executes the else function'''

a = input("Enter the value of a:")
a = int(a)

if (a>5):
    print("a is greater than 5.")
if (a>20):
    print("a is greater than 20.")
if (a>10):
    print("a is greater than 10.")
else: 
    print("a is lesser than 5.")

# If multiple ifs are used and input value satisfies multiple of them 
# then all the functions of those conditionals will carried out separately.