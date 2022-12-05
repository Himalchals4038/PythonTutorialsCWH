class Student :

    def __init__ (self) :
        self.__name = ""

    def getName (self) :
        return self.__name

    def setName (self, name) :
        self.__name = name

a = Student()
a.setName("Patel")
print(a.getName())

# Above one is without using any property getters. 
# We have to request the name as a function.

class Student :

    def __init__ (self) :
        self.__name = ""

    @property
    def getName (self) :
        return self.__name

    def setName (self, name) :
        self.__name = name

a = Student()
a.setName("Patel")
print(a.getName)

# Above one is using property getters. 
# We don't have to request name as function here.