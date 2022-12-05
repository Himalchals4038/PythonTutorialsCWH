'''Change value of list located inside a set.'''

a = {98, 62, 49, "Don", [25, 50]}
print(a)

# Here we will faulter in the first step when we try to print a list inside a set.
# Sets are unalterable whereas list is so set will not allow a list to be placed inside it.
# So question becomes wrong in the first place.

'''Even if we change that list into a tuple then also we can't alter it's data as tuple is unmutable.'''