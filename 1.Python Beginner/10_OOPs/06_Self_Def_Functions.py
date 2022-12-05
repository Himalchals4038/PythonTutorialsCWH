# class Employee :
#     company = "Tesla"
#     def getSalary() :
#         print("Salary is 130k")
#Above program will show error as nothing is defined under getSalary.

class Employee :
    company = "Tesla"
    def getSalary(self) :
        print("Salary is 130k")

# This is a iteration of the previous program using def function inside class attribute. 

Gajendra = Employee()

Gajendra.getSalary()  
Employee.getSalary(Gajendra)  