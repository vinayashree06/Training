#Hybrid inheritance unit testing
import unittest
class Animal:
    def speak(self):
        return "Animal speaks"
class Mammal(Animal):
    def walk(self):
        return "Mammal walks"
class Dog(Mammal):
    def speak(self):
        return "Dog barks"
class TestHybridInheritance(unittest.TestCase):
    def test_animal_speak(self):
        animal = Animal()
        self.assertEqual(animal.speak(), "Animal speaks")
    def test_mammal_walk(self):
        mammal = Mammal()
        self.assertEqual(mammal.walk(), "Mammal walks")
    def test_dog_speak(self):
        dog = Dog()
        self.assertEqual(dog.speak(), "Dog barks")
    def test_dog_inheritance(self):
        dog = Dog()
        self.assertEqual(dog.walk(), "Mammal walks")
if __name__ == '__main__':
    unittest.main()