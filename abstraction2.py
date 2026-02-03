from abc import ABC,abstractmethod
class Person(ABC):
    def __init__(self,name):
        self.name=name
    @abstractmethod
    def habit(self):
        pass
    def display_name(self):
        print(f"Dog's name:{self.name}")
class Labrador(Dog):
    def sound(self):
        print("Labrador Woof!")
d=Labrador("XYZ")
print(d.sound(),d.display_name())