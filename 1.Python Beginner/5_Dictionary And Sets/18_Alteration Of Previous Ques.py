'''Here the names of third and fourth friend is same. So note change in output.'''

a = {}

F1 = input("Enter favourite language of Sam: ")
F2 = input("Enter favourite language of Tom: ")
F3 = input("Enter favourite language of Dick: ")
F4 = input("Enter favourite language of Dick: ")

b = {
    "Sam": F1,
    "Tom": F2,
    "Dick": F3, 
    "Dick": F4
}

a.update(b)

print(a)

# Here the output is coming out to be the second language of Dick.
# This is because when we enter the favourite language of Dick for second time the first value get updated into the second value.
# This is possible in List and Dictionary. In Tuples and Sets error code will be shown.