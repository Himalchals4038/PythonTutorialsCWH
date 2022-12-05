class Employee :
    company = "Tesla" # Default Class Attribute
    def getSalary(self) :
        print(f"Salary for this employee working in {self.company} is {self.salary}")

# This is a iteration of the previous program using set inside def function.
# Here the coder will need to provide information about the salary of Gajendra after class attribute.

Gajendra = Employee()
Gajendra.salary = "112k" # Instance Attribute given

Gajendra.getSalary()