class Employee :
    company = "Samsung"

    def showDetails(self) :
        print("Employee Created")

# Programmer is a sister class of Employee.
# Sister class may contain some addtional attributes alongwith base class.
class Programmer(Employee) :
    language = "Python"

    def getLanguage(self) :
        print(f"The language is {self.language}")

e = Employee()
e.showDetails()
print(e.company)
# e.getLanguage()  This will show error as getLanguage is not defined under Employee, it is defined under Programmer.

p = Programmer()
p.showDetails()
print(p.company) # As company is not defined in sister class it will take from base class and print the details.
p.getLanguage()