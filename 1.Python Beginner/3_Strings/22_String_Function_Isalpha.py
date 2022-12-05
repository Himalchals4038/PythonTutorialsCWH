a = 'Tommorow' #is his eighteenth birthday.'
print(a.isalpha())
print(a.isdigit())

# isalpha searches if the given strings has only alphabets and returns true or false as answer.
# isalpha returns false even is there is one empty space or number or special character in the string.

b = '18'
print(b.isalpha())
print(b.isdigit())

# is digit does the same function except it searches for numbers.

c = '18th'
print(c.isalpha())
print(c.isdigit())
print(c.isalnum())

# is alnum searches for both alphabets and numbers.