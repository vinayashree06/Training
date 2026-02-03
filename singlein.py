
#Single inheritance unit testing 
import unittest
class Animal:
    def speak(self):
        return "Animal speaks"
class Dog(Animal):
    def speak(self):
        return "Dog barks"  
class TestAnimalInheritance(unittest.TestCase):
    def test_animal_speak(self):
        animal = Animal()
        self.assertEqual(animal.speak(), "Animal speaks")
    def test_dog_speak(self):
        dog = Dog()
        self.assertEqual(dog.speak(), "Dog barks")
if __name__ == '__main__':
    unittest.main()
