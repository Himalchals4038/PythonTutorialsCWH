class Employee :
    company = "Google" # Default Class Attribute
    salary = "100k" # Default Class Attribute

# Defining class of Manish and Rajendra.
Manish = Employee()
Rajendra = Employee()

print(Manish.company)
print(Rajendra.company)
print(Manish.salary)
print(Rajendra.salary)

# Creating Instance Attributes for both the objects.
Employee.company = "YouTube"
Manish.salary = "110k" # Instance Attribute
Rajendra.salary = "120k" # Instance Attribute

print(Manish.company)
print(Rajendra.company)
print(Manish.salary)
print(Rajendra.salary)

# print(Manish.address) will show error as there is no attribute for address in the program.
# Instance attribute modifies the data already provided by the class attribute and places itself in the place instead.