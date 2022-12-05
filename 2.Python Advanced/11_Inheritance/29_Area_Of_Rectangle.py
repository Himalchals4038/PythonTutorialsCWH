class Area :
    def findArea (self, a = None, b = None) :
        if a != None and b != None :
            print(f"Area of Rectangle is {a*b}")
        elif a != None and b == None :
            print(f"Area of Square is {a**2}")
        else :
            print("Nothing to find !!")

a = Area()
a.findArea(15, 22)
a.findArea(10)
a.findArea()