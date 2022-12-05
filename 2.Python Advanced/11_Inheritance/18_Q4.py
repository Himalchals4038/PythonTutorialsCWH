'''Write a program to show the addition and multiplication of 2 complex numbers.'''

class Complex :
    def __init__(self, r, i) :
        self.real = r
        self.imaginary = i
    
    def __add__(self, c) :
        return Complex(self.real + c.real, self.imaginary + c.imaginary)
    
    def __mul__(self, c) :
        return Complex(self.real * c.real - self.imaginary * c.imaginary, self.real * c.imaginary + self.imaginary * c.real)      

    def __str__(self) :
        return f"{self.real} + {self.imaginary}i"  

c1 = Complex(5, 6)
c2 = Complex(9, 1) 
print(c1 + c2)  
print(c1 * c2)