# Filter sorts out elements of the list which satisfy the given conditions and.
# Syntax : list(filter(function, list))

def num_greater_than_5 (num) :
    if num > 5 :
        return True
    else :
        return False

f10 = lambda num : num > 10
l = [3, 11, 4, 90, 7.2, 4.83, 29, 9.07]

print(list(filter(num_greater_than_5, l)))
# Above line prints the numbers greater than 5 present in the list.

print(list(filter(f10, l)))
# Above line prints the numbers greater than 10 present in the list.
# Lambda functions can also tbe used to shorten the code instead of def functions.

