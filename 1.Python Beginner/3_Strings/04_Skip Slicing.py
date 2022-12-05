'''We can skip letters in between the slicing by putting the skip number after close number separated with a colon.'''

name = "KapoorAndSons"
print(name[0::1])
# This will have no effect as 1 means printing all mentioned letters.
print(name[0:14:2])
# This will print result with one letter skipped after one letter. So result will be KpoAdos.
print(name[::3])
# This will print result with two letters skipped after every one letter. So result will be KoASs.
print(name[:14:4])
# this will print result with three letters skipped after every one letter. So result will be Kods.