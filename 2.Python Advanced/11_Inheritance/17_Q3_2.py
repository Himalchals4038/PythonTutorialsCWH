'''Alter of previous question with increment as multiple of base value instead of an independent value.'''

class Employee :
    company = "Panasonic"

    def paymentInfo(self, salary, increment) :
        self.salary = salary
        self.increment = increment

    @property
    def totalSalary(self) :
        return self.salary * self.increment
    
    @totalSalary.setter 
    def totalSalary(self, val):
        self.increment = val/self.salary
    
e = Employee()
e.paymentInfo(500, 1.6)
print(e.totalSalary)

e.totalSalary = 750
print(e.salary)
print(e.increment)

