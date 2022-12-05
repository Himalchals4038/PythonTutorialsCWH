a = [15, 26, 49, 36, 79, 49, 36, 80]
b = []
c = []

# for item in a :
#     if item%2 == 0 :
#         b.append(item)
#     else :
#         c.append(item)
# Above code is the general method to distinguish even and odd numbers.


b = [i for i in a if i%2 == 0]
c = [i for i in a if i%2 != 0]
# Above is the one-liner code to separate even and odd numbers.

print(b)
print(c)

d = []
d = [i for i in a if i>50]
print(d)

t = [5, 1, 6, 9, 6, 1, 2, 5, 7]
s = {i for i in t}
print(s)
