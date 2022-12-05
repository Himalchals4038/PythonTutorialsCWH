class Wipro :
    
    def DisplayInfo (self, name = ''):
        print("Welcome to Wipro India " + name)
    # name = '' denotes that name is a string and only string variables can be assigned to it.

a = Wipro()
a.DisplayInfo()

b = Wipro()
b.DisplayInfo("Anurag")
# In second case we are overwriting the value of the string from '' to 'Anurag'.