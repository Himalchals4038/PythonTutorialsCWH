'''
Write a program to display the table of 7 column-wise.
'''

# l = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
l = [str(i*7) for i in range (1,11)]

# for item in l :
#     print(item, "\n")

a = "\n".join(l)
print(a)



