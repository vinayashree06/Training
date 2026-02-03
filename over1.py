class Cat:
    def speak(self):
        return "Meow"
class Dog:
    def speak(self):
        return "Bow Bow"
def make(animal):
    return animal.speak()
print(make(Cat()))
print(make(Dog()))