class Employee :
    company = "Tesla" 

    # __init__ is a constructor. Python runs this function before anything else of the class.
    def __init__(self, name, salary, subunit) :
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is created")
    
    def getDetails(self) :
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The subunit of the employee is {self.subunit}")

    def getSalary(self, signature) :
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet() :
        print("Good Morning, Sir")

    @staticmethod
    def time() :
        print("It is 9AM in the morning.")

Akshay = Employee("Akshay Raj", 9000, "SDE")
# Akshay = Employee() Throws an error as no information is provided about Akshay in the form of name, salary and subunit.
Akshay.greet()
Akshay.getDetails()
 