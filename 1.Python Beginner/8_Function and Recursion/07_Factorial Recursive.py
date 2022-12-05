# def factorial_iter(a):
#     p = 1
#     for i in range (a):
#         p = p * (i+1)
#         i = i + 1
#     return p
# a = int(input("Enter the number you want to find factorial of: "))
# f = (factorial_iter(a))
# print(f)

# Recursion is a mathematical function that calls itself.

def factorial_recursive(n):
    if n == 1 or n == 0 :
        return 1
    else :
        return n * factorial_recursive(n-1)

a = int(input("Enter the number you want to find factorial of: "))

f = (factorial_recursive(a))

print(f)

# Recursive function repeats the command assigned to it with the value before or after the first value.