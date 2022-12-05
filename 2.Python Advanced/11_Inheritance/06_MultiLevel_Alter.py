class Person :
    country = "India"

    def takeBreath(self) :
        print("I am breathing...")

class Employee(Person) :
    company = "Honda"

    def getSalary(self) :
        print(f"Salary is {self.salary}")
    
    def takeBreath(self) :
        print("i am Employee so I am luckily breathing...")
    
class Programmer(Employee):
    company = "Fiverr"

    def getSalary(self) :
        print("No salary to programmers")
    
    def takeBreath(self) :
        print("I am Programmer so I am breathing...")

p = Person()
p.takeBreath()
# print(p.company) throws an error as no campany is specfied

e = Employee()
e.takeBreath()
print(e.company)

pr = Programmer()
pr.takeBreath()
print(pr.company)
print(pr.country)
