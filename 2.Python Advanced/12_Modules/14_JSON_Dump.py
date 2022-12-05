'''
JSON stands for JavaScript Object Notation
It is mainly used for storing snd transferring data between browwser and server.
Python supports JSON with a built-in package called json.
JSON supports mainly 6 data types -> string, number, boolean, null, object, array.
'''
import json

p = {"name" : "GeeksForGeeks", 
    "Language" : ["Python", "Java", "C++", "Ruby"]
    }
# In Python JSON exists as a string.

print(type(p))
f = json.dumps(p)
print(type(f))
print(f)

# Dumps changes the dictionary to JSON string.