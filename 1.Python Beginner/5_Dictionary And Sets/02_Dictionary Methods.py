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
print(myDict.keys())
print(myDict.values())
print(type(myDict.keys()))
print(list(myDict.keys())) # Prints the keys of the Dictionary.
print(list(myDict.values())) # Prints the values of the Dictionary.
print(list(myDict.items())) # Prints the keys alongwith values in tuples of the Dictionary.
