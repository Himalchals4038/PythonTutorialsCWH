def multiply(n):
    for i in range (1,21):
        j = n * i
        print(n, "X", i, "=", j)
        i = i + 1

a = int(input("Enter the number whose multiplication table you want to see: "))

b = multiply(a)

print(b)