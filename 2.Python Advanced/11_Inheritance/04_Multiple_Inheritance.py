class Employee : 
    company = "Cisco"
    eCode = 125
# This is Parent 1.

class FreeLancer :
    company = "Fiverr"
    level = 3

    def upgradeLevel(self) :
        self.level = self.level + 1
# This is Parent 2.

class Programmer(Employee, FreeLancer) :
    name = "Priyangshu"
# This is the Child class. It contains attributes of both parents.

p = Programmer()
print(p.company) 
# This prints on priority basis. As Employee is first mentioned in Programmer so Cisco is printed. 
# If FreeLancer was mentioned first in Programmer then Fiverr would have been printed.
print(p.eCode)
p.upgradeLevel()
print(p.level)