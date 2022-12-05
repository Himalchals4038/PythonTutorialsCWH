a = "Welcome to the amazing {} world of Tarzan {} Jungle Boy".format('fun-filled', 'the')
print(a)
# When nothing is given in the brackets 0, 1, 2, .. is taken as default in each of the consecutive strings.
# 'fun-filled' is assigned to 0, 'the' to 1 as so on.

a = "Welcome to the amazing {0} world of Tarzan {1} Jungle Boy".format('fun-filled', 'the')
print(a)
# When given index number the values under format are accrodingly placed in matching index locations.

a = "Welcome to the amazing {1} world of Tarzan {0} Jungle Boy".format('fun-filled', 'the')
print(a)
# The index numbers need not necessarily be in succession. They can be in random arrangements.

a = "Welcome to the amazing {0:20} world of Tarzan {1} Jungle Boy".format('fun-filled', 'the')
print(a)

# We can also define the space oocupied by that index by specifying the number of digits after
# the index number separated by a colon. If the value assigned to the index doesn't has that big length 
# it will fill the space at last and leave the beginning spaces empty.

'''
a = "Welcome to the amazing {2} world of Tarzan {1} Jungle Boy".format('fun-filled', 'the')
print(a)
Specifying index numbers out of the range of number of variables specified in the format space will result in error.
For eg. value with index number 2 i.e. third variable doesn't exist in format box so program returns an error.
'''

a = "Welcome to the amazing {0:^20} world of Tarzan {1} Jungle Boy".format('fun-filled', 'the')
print(a)
# ^ character if the centre indentation of the value in the middle of the digit space alloted by the coder.

a = "Welcome to the amazing {0:>20} world of Tarzan {1} Jungle Boy".format('fun-filled', 'the')
print(a)
# > character is the default right indentation with value on right-end of the digit space provided.

a = "Welcome to the amazing {0:<20} world of Tarzan {1:^10} Jungle Boy".format('fun-filled', 'the')
print(a)
# < character is the left indentation of the value on the left-end of the digit space provided.