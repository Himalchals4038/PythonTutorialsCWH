class Student :
    __name = 'Dinesh'
    grade = 10

a = Student()
print(a.grade)
print(a.__name)

# '__name' can't be printed directly as '__' is encapsulation symbol. 
# Thus the data inside 'name' will be encapsulated.
# 'grade' not being under encapsulation can be accessed dierectly.