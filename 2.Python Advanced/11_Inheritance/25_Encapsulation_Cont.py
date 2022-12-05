class Student :
    __name = 'Dinesh'
    grade = 10

    def __init__ (self) :
        print(self.__name)
        self.__displayInfo()
    
    def __displayInfo(self) :
        print("Welcome to ")

a = Student()
print(a.grade)

# If we put encapsulated data inside a function only then can it be accessed.
