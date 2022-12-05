'''Fill up a Railway Application Form using Oops method.'''

class RailwayForm :
    formtype = "RailwayForm"
    def printData(self) :
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")
    
robertsApplication = RailwayForm()
robertsApplication.name = "Robert Spencer"
robertsApplication.train = "Purva Express"
robertsApplication.printData() 