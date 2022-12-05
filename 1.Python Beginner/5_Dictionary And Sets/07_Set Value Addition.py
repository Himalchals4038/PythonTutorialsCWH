# Add Syntax adds the value to the set.
# If a value is added multiple times then also it will be added only one time.
# If a value is already added in the set and we try to add it once more then no changes will occur in the set.

b = set()
b.add(1)
b.add(8)
b.add(5)
b.add(5)
b.add(5) 

# b.add([25, 15, 35, 45]) # We cannot add list inside a set.
# This is because we can change value inside a list but we cannot do it inside a set.

b.add((15, 35, 65, 29))
# We can add tuple inside a set.
# Tupple value cannot be changed once defined so it can be included inside a set.

# b.add({15 : 26}) # We cannot add dictionary inside a set.
# Dictionary values can be changed so they are not included inside a set.

print(b)