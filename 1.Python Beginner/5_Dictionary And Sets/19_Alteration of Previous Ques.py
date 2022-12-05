'''Here the favourite languages of Tom and Dick are the same. Note changes in results.'''

a = {}

F1 = input("Enter favourite language of Sam: ")
F2 = input("Enter favourite language of Tom: ")
F3 = input("Enter favourite language of Dick: ")
F4 = input("Enter favourite language of Harry: ")

b = {
    "Sam": F1,
    "Tom": F2,
    "Dick": F3, 
    "Harry": F4
}

a.update(b)

print(a)

# No changes observed as each value is denoted to its respective index and there is no conflict. 
# Even if 2 values are same, their indexes are different.