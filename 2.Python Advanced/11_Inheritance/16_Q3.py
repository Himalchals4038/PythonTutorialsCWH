'''Write a program to print total salary of an employee after increment.
Later add ceiling salary of the employee and show max increment possible.'''

class Employee :
    company = "Panasonic"

    def paymentInfo(self, salary, increment) :
        self.salary = salary
        self.increment = increment

    @property
    def totalSalary(self) :
        return self.salary + self.increment
    
    @totalSalary.setter 
    def totalSalary(self, val):
        self.increment = val - self.salary
    
e = Employee()
e.paymentInfo(500, 150)
print(e.totalSalary)

e.totalSalary = 620
print(e.salary)
print(e.increment)

