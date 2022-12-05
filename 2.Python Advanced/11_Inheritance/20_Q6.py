'''Write a program to display the 3D vectors in i j k form.'''

class Vector :
    def __init__(self, vec) :
        self.vec = vec

    def __str__(self) :
        return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"
 
v1 = Vector([1, 4, 6])
v2 = Vector([2, 8, 5])
print(v1)
print(v2)
