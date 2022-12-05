'''Print the star pattern 2 and show the user no. of rows he/she wants.'''

n = int(input("Enter the number of patterns you want to see: "))


for i in range (0, n):
    print(" " * (n-i-1), end = "")
    print("*" * (2*i+1), end = "")
    print(" " * (n-i-1))

# end = "" makes all the print functions print one next to other and not in separate rows.