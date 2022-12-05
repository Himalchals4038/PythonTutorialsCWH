'''Setter property decorator sets a standard value for a function and other values have to comply and modify accordingly to it.'''

class Employee :
    company = "HPCL"

    def inputDetails(self, salary, bonus) :
        self.salary = salary
        self.bonus = bonus

    @property 
    def totalSalary(self) :
        return self.salary + self.bonus
    
    @totalSalary.setter # --> This is a setter property.
    def totalSalary(self, val):
        self.bonus = val - self.salary 

e = Employee()
e.inputDetails(5260, 943)
print(e.totalSalary)

e.totalSalary = 6000
print(e.salary)
print(e.bonus)