a = int(input("Enter the number upto which sum and product is to be found: "))

def factorial_sum_recursive(n):
    if n == 1 or n == 0 :
        return 1
    else :
        return n + factorial_sum_recursive(n-1)

def factorial_product_recursive(n):
    if n == 1 or n == 0 :
        return 1
    else :
        return n * factorial_product_recursive(n-1)

s = factorial_sum_recursive(a)
p = factorial_product_recursive(a)

print("The sum of all natural numbers upto ",a, " is: ", s)
print("The product of all natural numbers upto ",a, " is: ", p)