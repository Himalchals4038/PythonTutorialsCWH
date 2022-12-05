'''Write a program to display 2D and 3D coordinates in form of i-cap, j-cap, k-cap.'''

class C2dVec :

    def __init__(self, i, j) :
        self.icap = i
        self.jcap = j

    def __str__(self) :
        return f"{self.icap}i + {self.jcap}j"
        
class C3dVec(C2dVec) :

    def __init__(self, i, j, k) :
        super().__init__(i, j)
        self.kcap = k
    
    def __str__(self) :
            return f"{self.icap}i + {self.jcap}j + {self.kcap}k"

v2d = C2dVec(2, 6)
v3d = C3dVec(9, 4, 7)
print(v2d)
print(v3d)