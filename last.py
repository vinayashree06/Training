from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print(self.name, "barks")
class Cat(Animal):
    def sound(self):
        print(self.name, "meows")
animals = [Dog("Buddy"), Cat("Kitty")]
for animal in animals:
    animal.sound()
