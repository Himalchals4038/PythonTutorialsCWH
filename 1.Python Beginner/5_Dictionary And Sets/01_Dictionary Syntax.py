# {}symbol is used to depict a dictionary in which data and their meaning is provided by the coder.
# In Dictionary the first value is called keys and second one is called values.

myDict = {
    "Python": "A Programming Language",
    "HC Verma": "Physics Teacher",
    "Roll Number": (6, 2, 9, 3, 8), # Dictionary can also store lists and tuples assigned to a specific variable by the coder.
    "War": "Loss Of Lives and Property",
    "ChosenArchitect": "Minecraft Player",
    "Marks": [12, 15, 20],   
    "Dict1": {"Harry": "Python Basics"} # One Dictionary can be formed inside another dictionary.
}  

myDict['Marks'] = [25, 37, 60]
# The Dictionary list values can also be modified or changed as per requirement.
# Obviously tuple values can't be changed once assigned.

print(myDict['War'])
print(myDict['Roll Number'])
print(myDict['ChosenArchitect'])
print(myDict['Marks'])
print(myDict['Dict1']['Harry'])
# Secondary Dictionary inside the main dictionary can be accessed by writing secondary dictionary name followed by the required variable.

print(myDict['Roll Number'].index(3)) 
# We can even find index of required value located inside a tuple of Dictionary.

