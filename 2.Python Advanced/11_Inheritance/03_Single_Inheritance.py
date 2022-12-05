'''Below is an example of single inheritance where the sister class is derived from a single base class.'''

class Employee :
    company = "Samsung"

    def showCompany(self) :
        print(f"The company is {self.company}")

    def showDetails(self) :
        print("Employee Created")

class Programmer(Employee) :
    language = "Python"
    company = "Smartphones" 

    def showCompany(self) :
        print(f"The company is {self.company}")

    def getLanguage(self) :
        print(f"The language is {self.language}")
    
    def showDetails(self) :
        print("Programmer Created") 

e = Employee()
e.showDetails()
e.showCompany()

p = Programmer()
p.showDetails()
p.showCompany() 
p.getLanguage()