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

print(myDict)
updateDict = {
    "C++": "Used to make games",
    "Bhavnesh": "Good Friend",
    "HC Verma": "Author Of Concepts Of Physics"
}
myDict.update(updateDict)

print(myDict)

# Update command updates the dictionary by adding key-value pairs from updateDict. 
# It also alters the old value of key with new one if there is a replacement available.