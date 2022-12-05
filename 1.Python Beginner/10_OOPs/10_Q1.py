'''Write a python program to store information of few programmers working at Microsoft.'''

class Programmer :
    company = "Microsoft"
    def __init__(self, name, sector, salary) :
        self.name = name
        self.sector = sector
        self.salary = salary
        print("Employee Created")

    def getDetails(self) :
        print(f"The name of employee is {self.name}")
        print(f"The sector of employee is {self.sector}")
        print(f"The salary of employee is {self.salary}")
    
Tim = Programmer("Tim Handerson", "Frontend Designer", "250k")
Dick = Programmer("Dick Somerfield", "Server Regulator", "240k")
Dan = Programmer("Dan TDM", "Backend Fixer", "280k")
Sanna = Programmer("Sanna Samson", "Frontend Publisher", "215k")

Tim.getDetails()
Dick.getDetails()
Dan.getDetails()
Sanna.getDetails()