'''
def func(a) :
    return a+5
x = 433
print(func(x))
'''

func = lambda a : a+5
x = 433
print(func(x))

# Lambda is like a replacement for def function to make the code shorter.
# It can be assigned any function like addition, substraction, division, square, cube, etc.

sum2 = lambda a,b : a+b
sum3 = lambda a,b,c : a+b+c
diff = lambda a,b : abs(a-b)
mul2 = lambda a,b : a*b
mul3 = lambda a,b,c : a*b*c
absdiv = lambda a,b : a/b
floordiv = lambda a,b : a//b
square = lambda a : a*a

print(square(x))
print(mul2(36, 49))
print(sum3(1825, 153, 769))
print(floordiv(35, 8))