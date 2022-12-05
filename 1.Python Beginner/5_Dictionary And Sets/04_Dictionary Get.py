myDict = {
    "Python": "A Programming Language",
    "HC Verma": "Physics Teacher",
    "Roll Number": (6, 2, 9, 3, 8), 
    "War": "Loss Of Lives and Property",
    "ChosenArchitect": "Minecraft Player",
    "Marks": [12, 15, 20],   
    "Dict1": {"Harry": "Python Basics"}, 
    150: 956
  
} 

print(myDict.get("Marks"))
print(myDict.get("Python"))
print(type(myDict.get("Python")))
print(myDict.get("Roll Number"))
print(myDict['Dict1']['Harry'])
print(myDict['War']) # This command will print same result as get command if the variable is present.

# Get command finds the appropiate key identical to one typed in get bracket and prints the value corresponding to it.
# Get command works with strings, lists ands tuples all.

print(myDict.get("Dict2")) # This will print None.
print(myDict['Dict2']) # This will show error.
# Get command will show none if index is not present in Dictionary.
# [] syntax will show error if index is not present in Dictionary.
