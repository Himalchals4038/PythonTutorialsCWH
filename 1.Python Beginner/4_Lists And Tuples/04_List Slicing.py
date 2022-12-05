'''List Slicing is same as string slicing with ability to use both positive and negative indexes as well as skips.'''

friends = ["Jack", "Carla", "Dorothy", "Nastra", "Holmes", 846]
print(friends[0:4])
print(friends[1:6:3])
print(friends[-5:-2])
print(friends[-5], friends[-2])
print(friends[-6::2])
