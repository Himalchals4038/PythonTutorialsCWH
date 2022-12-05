'''Write a program to display of sum of first n natural numbers.
Also accept the value of n from the user.'''

n = int(input("Enter the number of terms you want the sum of: "))

p = 0

for j in range (1, n+1):
    p = p + j

print("The sum of first", n, "natural numbers is", p)