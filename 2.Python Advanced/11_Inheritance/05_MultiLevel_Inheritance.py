class Employee :
    company = "Jio" # Parent 1
    state = "Maharashtra"

    def State(self) :
        print(f"The employee is working in {self.state}")
    
    def infoMedianSalary(self) :
        print("The median salary of this region is Rs.60000")

class Technical(Employee) :
    sector = "Development" # Child 1
    city = "Pune"
    
    def City(self) :
        print(f"The data centre is located in {self.city}")
    
    def infoMedianSalary(self) :
        print("The median salary of this region is Rs.80000")
    
    def Enquiry(self) :
        print(f"The enquiry has been registered in {self.state} Database.")

class Programmer(Technical) :
    website = "JioMart" # Child 2 ( Child of Child 1)
    department = "Website Maintenance"

    def Dept(self) :
        print(f"The person is working on {self.website} and his department is {self.department}")
    
    def infoMedianSalary(self) :
        print("The Median salary of the department is Rs.120000")

e = Employee()
t = Technical()
p = Programmer()

print(p.company)
print(p.sector)
print(p.website)

p.State()
p.City()
p.Dept()

e.infoMedianSalary()
t.infoMedianSalary()
p.infoMedianSalary()
