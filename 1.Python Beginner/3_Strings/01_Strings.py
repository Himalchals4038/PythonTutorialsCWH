# Single, double and triple coat have same function as both of them depict string value.
# We use double and triple coat when we already have used single and/or double coats in our variable.
# z = 'barry's home' will show error as system can't understand where the string is starting and where it is ending.

a = 'Kassandra'
b = "Tanmay's favourite" # --> Use double coat when single coat has already been used in the variable.
c = '''Kapoor and Son's and "Mittal's"''' # --> Use triple coat when both single and double coat has been used.
d = 'The "Archon" is here' # --> We can also use single coat if double coat has been used in the variable.
print(type(a))
print(type(b))
print(type(c))
print(type(d))
