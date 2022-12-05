import json

file = open('json_eg.json', 'r')
a = file.read()
b = json.loads(a)

print(b)
for c in b :
    print(c)
    