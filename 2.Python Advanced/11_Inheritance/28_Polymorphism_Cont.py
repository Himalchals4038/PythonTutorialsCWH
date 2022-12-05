class Reliance :

    def DisplayInfo(self) :
        print("Welcome to Reliance Industries, India")
    
class JIO(Reliance) :

    def DisplayInfo(self):
        super().DisplayInfo()
        print("Welcome to JIO Telecommunication Services, India")

a = JIO()
a.DisplayInfo()

# To display the parent class alongwith the child class we have to use super function.