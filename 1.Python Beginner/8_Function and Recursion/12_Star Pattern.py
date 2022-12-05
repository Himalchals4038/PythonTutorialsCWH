n = int(input("Enter the no. of rows of pattern you want to see: "))

def star_pattern(a):
    for i in range (a):
        print("*" * (a-i), end = "")
        print(" " * i)

k = star_pattern(n)

print(k)