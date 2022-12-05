'''Print the star pattern 3 and show the user no. of rows he/she wants.'''

a = int(input("Enter the number of patterns you want to see: "))

for i in range (0, a):
    if (i%2 == 0):
        print("*" * 3)
    else:
        print("*", end = "")
        print(" ", end = "")
        print("*")

# Here we show 3 stars at odd places and 2 stars with a gap between at even places.