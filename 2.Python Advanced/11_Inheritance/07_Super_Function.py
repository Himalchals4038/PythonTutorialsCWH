class Person :
    country = "India"

    def __init__(self) :
        print("Initializing Person")

    def takeBreath(self) :
        print("I am breathing...\n")

class Employee(Person) :
    company = "Honda"
    salary = 160000

    def __init__(self) :
        super().__init__()
        print("Initialzing Employee")

    def getSalary(self) :
        print(f"Salary is {self.salary}")
    
    def takeBreath(self) :
        super().takeBreath()
        print("I am Employee so I am luckily breathing...\n")
    
class Programmer(Employee):
    company = "Fiverr"

    def __init__(self) :
        super().__init__()
        print("Initializing Programmer")

    def getSalary(self) :
        print("No salary to programmers")
    
    def takeBreath(self) :
        super().takeBreath() # This also prints the preceding class attribute of takeBreath.
        print("I am Programmer so I am breathing...\n")

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


