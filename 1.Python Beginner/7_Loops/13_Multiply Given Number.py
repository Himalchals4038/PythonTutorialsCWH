'''Accept a number from user and then display its multiplication table till 20.'''

i = int(input("Enter your desired number: "))

j = 0

for j in range (0, 21):
    k = i*j
    print(i, "into", j, "is equal to", k)

print("Multiplication Done !!")