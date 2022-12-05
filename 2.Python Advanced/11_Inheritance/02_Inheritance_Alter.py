class Employee :
    company = "Samsung"

    def showCompany(self) :
        print(f"The company is {self.company}")

    def showDetails(self) :
        print("Employee Created")

# Programmer is a sister class of Employee.
# Sister class may contain some addtional attributes alongwith base class.
class Programmer(Employee) :
    language = "Python"
    company = "Smartphones" # This acts as an instance attribute and modifies base attribute for sister class.

    def showCompany(self) :
        print(f"The company is {self.company}")

    def getLanguage(self) :
        print(f"The language is {self.language}")
    
    def showDetails(self) :
        print("Programmer Created") # This acts as an instance attribute and modifies the base attribute for sister class.

e = Employee()
e.showDetails()
e.showCompany()
# e.getLanguage()  This will show error as getLanguage is not defined under Employee, it is defined under Programmer.

p = Programmer()
p.showDetails()
p.showCompany() # As company is not defined in sister class it will take from base class and print the details.
p.getLanguage()