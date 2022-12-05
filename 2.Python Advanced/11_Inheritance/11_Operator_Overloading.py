# '''This only prints 'Let's add' and 300.'''

# class Number :
#     def __init__(self, num) :
#         self.num = num

#     def __add__(self, num2) :
#         print("Let's add")
#         return 300

# n1 = Number(4)
# n2 = Number(6)
# sum = n1 + n2
# print(sum) 

'''This prints the required result properly and also prints 'Let's add'.'''

class Number :
    def __init__(self, num) :
        self.num = num

    def __add__(self, num2) :
        print("Let's add")
        return self.num + num2.num

    def __mul__(self, num2) :
        print("Let's multiply")
        return self.num * num2.num

n1 = Number(4)
n2 = Number(6)
sum = n1 + n2
print(sum)   
product = n1 * n2
print(product)     