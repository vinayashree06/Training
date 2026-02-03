#Hierarchical inheritance unit testing
import unittest
class Vehicle:
    def get_vehicle_type(self):
        return "Generic Vehicle"
class Car(Vehicle):
    def get_vehicle_type(self):
        return "Car"
class Bike(Vehicle):
    def get_vehicle_type(self):
        return "Bike"
class TestHierarchicalInheritance(unittest.TestCase):
    def test_vehicle_type(self):
        vehicle = Vehicle()
        self.assertEqual(vehicle.get_vehicle_type(), "Generic Vehicle")
    def test_car_type(self):
        car = Car()
        self.assertEqual(car.get_vehicle_type(), "Car")
    def test_bike_type(self):
        bike = Bike()
        self.assertEqual(bike.get_vehicle_type(), "Bike")
if __name__ == '__main__':
    unittest.main()