'''If we change the parameter of the class attribute does the result remains same then or not ??'''

class Sample :
    def __init__(self, name) :
        self.name = name

obj = Sample("Turner")        
print(obj.name)

class Sample :
    def __init__(Turner, name) :
        Turner.name = name

obj = Sample("Turner")        
print(obj.name)

class Sample :
    def __init__(slf, name) :
        slf.name = name

obj = Sample("Turner")        
print(obj.name)

# Yes if we change the parameter of class attribute then also the result remains same.