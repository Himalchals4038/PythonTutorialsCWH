'''Getter property decorator finds out required value from other values given in code or supplied by user.'''

class Employee :
    company = "HPCL"

    def inputDetails(self, salary, bonus) :
        self.salary = salary
        self.bonus = bonus

    @property # --> This is a getter property.
    def totalSalary(self) :
        return self.salary + self.bonus

e = Employee()
e.inputDetails(5260, 943)
print(e.totalSalary)
# By adding propery decorator @property we don't have to display total salary as a function.

class Employee :
    company = "HPCL"

    def inputDetails(self, salary, bonus) :
        self.salary = salary
        self.bonus = bonus

    # @property
    def totalSalary(self) :
        return self.salary + self.bonus

e = Employee()
e.inputDetails(5260, 943)
print(e.totalSalary())

# Without putting property decorator we have to find out total salary as a property.