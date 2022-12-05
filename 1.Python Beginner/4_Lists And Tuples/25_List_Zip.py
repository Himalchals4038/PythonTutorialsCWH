l1 = [10, 30, 50, 70, 90, 110]
l2 = [11, 22, 33, 44, 66, 99, 88]

for a,b in zip(l1,l2) :
    print(a,b)

# Zip Function is used to diplay the elements of two or more lists side by side.
# Zip prints side by side the elements of each list with same index.
# If lists have different number of values, zip will stop at lowest index and not print the elements of other lists beyond that index number.

t = min(len(l1), len(l2))
for i in range (t) :
    print(l1[i], l2[i])
# Above is the general way to print the values side by side which is shortened by using zip function.