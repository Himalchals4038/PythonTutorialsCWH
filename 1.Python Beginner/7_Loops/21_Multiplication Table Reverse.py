'''Write a program to print the multiplcation table of the number given by the user upto 20.'''

a = int(input("Enter your desired number: "))

for i in range (1, 21):

    k = a * (21-i)

    print(a, "X", (21-i), "=", k)

print("Above is the reverse multiplication table upto 20 of", a)