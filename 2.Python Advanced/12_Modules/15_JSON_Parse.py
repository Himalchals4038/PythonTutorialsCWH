import json

a = '{"Tom":"Director", "Sam":"Caretaker", "Gill":"Stylist", "Agatha":"Technician"}'
print(type(a))
b = json.loads(a)
print(type(b))
print(b)

for c in b :
    print(c, b[c]) # Prints the key values of the dictionary.

# Parse changes JSON string to dictionary.

d = '[{"Tom":"Director", "Sam":"Caretaker", "Gill":"Stylist", "Agatha":"Technician"}]'
print(type(d))
e = json.loads(d)
print(type(e))
print(e)

# Parse changes JSON string to list.