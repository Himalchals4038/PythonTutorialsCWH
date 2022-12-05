class Calculator :

    def __init__(self, number) :
        self.number = number
        print("Data intaken")

    def square(self) :
        print(f"The square of {self.number} is {self.number ** 2}")

    def cube(self) :
        print(f"The cube of {self.number} is {self.number ** 3}")

    def squareRoot(self) :
        print(f"The square root of {self.number} is {self.number ** (1/2)}")

    def cubeRoot(self) :
        print(f"The cube root of {self.number} is {self.number ** (1/3)}")
    
    @staticmethod
    def greet() :
        print("******Hello there welcome to the best calculator in python*******")

a = Calculator(int(input("Enter your desired number: ")))

a.greet()
a.square()
a.cube()
a.squareRoot()
a.cubeRoot()