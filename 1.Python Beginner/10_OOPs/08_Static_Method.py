class Employee :
    company = "Tesla" # Default Class Attribute
    def getSalary(self, signature) :
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")
    # Signature prints the value given in () after the attribute.

    @staticmethod
    def greet() :
        print("Good Morning, Sir")
    # Static method states that you don't need attribute to print it.
    # def greet(self) will show error as attribute is being given to it.

    @staticmethod
    def time() :
        print("It is 9AM in the morning.")

Gajendra = Employee()
Gajendra.salary = "112k"


Gajendra.greet()
Gajendra.time()
Gajendra.getSalary("Gajendra Sekhawat")