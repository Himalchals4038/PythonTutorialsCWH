class Employee :
    company = "TCS"
    salary = "95000" # Class Attribute
    location = "Patna"
    
    def changeSalary(self, sal) :
        self.salary = sal # Instance Attribute

e = Employee()
print(e.salary)

e.changeSalary(115000)
print(e.salary) # Prints instance attribute

print(Employee.salary) # Prints class attribute

'''Above one doesn't change class attribute, it only adds an instance attribute.'''

class Employee :
    company = "TCS"
    salary = "95000" 
    location = "Patna"
    
    def changeSalary(self, sal) :
        self.__class__.salary = sal 

e = Employee()
print(e.salary)

e.changeSalary(115000)
print(e.salary) 

print(Employee.salary) 

'''Above one changes class attribute instead of adding an instance attribute.'''

class Employee :
    company = "TCS"
    salary = "95000" 
    location = "Patna"
    
    @classmethod
    def changeSalary(cls, sal) :
        cls.salary = sal 

e = Employee()
print(e.salary)

e.changeSalary(115000)
print(e.salary) 

print(Employee.salary) 

'''Above one is another method of changing class attribute by adding @classmethod.'''
