'''Write a program to display bark of class Dog included under class Pets included under class Animals'''

class Animals :
    animalType = "Mammal"

class Pets(Animals):
    petType = "Household"
    petColor = "Gray"

class Dog(Pets):

    @staticmethod
    def bark():
        print("Bow Bow")

d = Dog
print(d.animalType)
print(d.petType)
print(d.petColor)
d.bark()
