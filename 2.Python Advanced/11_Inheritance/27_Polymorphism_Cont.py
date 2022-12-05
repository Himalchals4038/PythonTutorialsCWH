class Reliance :

    def DisplayInfo(self) :
        print("Welcome to Reliance Industries, India")
    
class JIO(Reliance) :

    def DisplayInfo(self):
        print("Welcome to JIO Telecommunication Services, India")

a = JIO()
a.DisplayInfo()
# Here the child class JIO is replacing the DisplayInfo function 
# of parent class Reliance by its own DisplayInfo function.