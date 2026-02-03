#create an abstract class Vehicle, All vehicles must implement a method start(), Task: Ensure that child classes provide their own implementation of start(), use pytest
import pytest
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class Car(Vehicle):
    def start(self):
        return "Car started"
class Bike(Vehicle):
    def start(self):
        return "Bike started"
def test_vehicle_start():
    car = Car()
    bike = Bike()
    assert car.start() == "Car started"
    assert bike.start() == "Bike started"
if __name__=="__main__":
    pytest.main()