#Multiple inheritance unit testing
import unittest
class Person:
    def get_name(self):
        return "Person Name"    
class Employee:
    def get_employee_id(self):
        return "EMP123" 
class Manager(Person, Employee):
    def get_manager_details(self):
        return f"{self.get_name()} - {self.get_employee_id()}"
class TestMultipleInheritance(unittest.TestCase):
    def test_person_name(self):
        person = Person()
        self.assertEqual(person.get_name(), "Person Name")
    def test_employee_id(self):
        employee = Employee()
        self.assertEqual(employee.get_employee_id(), "EMP123")
    def test_manager_details(self):
        manager = Manager()
        self.assertEqual(manager.get_manager_details(), "Person Name - EMP123")
if __name__ == '__main__':
    unittest.main()