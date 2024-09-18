from animal import Animal
class Dog(Animal):
    def bark(self):
        return "barking..."
    
lau = Dog()
print(lau.eat())
print(lau.bark())