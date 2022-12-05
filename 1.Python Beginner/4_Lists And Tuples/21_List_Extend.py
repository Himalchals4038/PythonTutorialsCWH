l1 = [79, 39, 80, -61, 0, 53]
l2 = [15, 36, 88]
l3 = [66, 22, 81, 72, 14]
l4 = [-5, 3]

l1.append(l2)
print(l1)
# Append adds the l2 list as a whole entity under l1 list.

l3.extend(l4)
print(l3)
# Extend adds the elements of l4 into l3 list.