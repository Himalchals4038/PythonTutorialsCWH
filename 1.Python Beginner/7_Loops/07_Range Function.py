# Range (n) means 0 to n-1. 

for i in range (8):
    print(i)
else:
    print("Done")
# Giving one value in bracket will be considered as last value and first value is considered as 0. 

for j in range (1, 8):
    print(j)
else:
    print("Done")
# Giving two values in bracket will consider first at beginning and second as last last.

for k in range (0, 8, 2):
    print(k)
else:
    print("Done")
# Third number in bracket denotes step size. Above one will print (0, 2, 4, 6).


