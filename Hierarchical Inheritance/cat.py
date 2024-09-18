from animal import Animal
class Cat(Animal):
    def meow(self):
        return "meowing..."
    
nuong = Cat()
print(nuong.eat())
print(nuong.meow())