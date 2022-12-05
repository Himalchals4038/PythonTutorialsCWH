'''Write a program to detect if both the given vectors have same number of dimension or not.
If not then when we try to add or multiply them, an eror code is shown as answer.'''

class Vector1 :
    def __init__(self, vec):
        self.vec = vec
    
    def __len__(self) :
        return len(self.vec)

v1 = Vector1([6, 2])
v2 = Vector1([1, 8]) 

p = (len(v1))
q = (len(v2))

if p == q :
    class Vector :
        def __init__(self, vec) :
            self.vec = vec
    
        def __str__(self) :
            str1 = ""
            index = 0
    
            for i in self.vec :
                str1 += f" {i}a{index} +"
                index += 1
            return str1[:-1]
        
        def __add__(self, vec2) :
            newList = []
            for i in range(len(self.vec)):
                newList.append(self.vec[i] + vec2.vec[i])
            return Vector(newList)
    
        def __mul__(self, vec2) :
            sum = 0
            for i in range(len(self.vec)):
                sum += self.vec[i] * vec2.vec[i]
            return sum

    v1 = Vector([6, 2])
    v2 = Vector([1, 8]) 

    print(v1 + v2)
    print(v1 * v2)
else :
        print("Both vectors don't have same dimensions !!")



