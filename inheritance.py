#You are given a base class Employee, Classes Manager and Developer should inherit common properties, Task:Reuse code using inheritance and avoid duplication, use pytest
import pytest
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name,salary)
        self.department=department
class Developer(Employee):
    def __init__(self,name,salary,programming_language):
        super().__init__(name,salary)
        self.programming_language=programming_language
def test_employee_inheritance():
    manager = Manager("Alice", 90000, "HR")
    developer = Developer("Bob", 80000, "Python")
    assert manager.name == "Alice"
    assert manager.salary == 90000
    assert manager.department == "HR"
    assert developer.name == "Bob"
    assert developer.salary == 80000
    assert developer.programming_language == "Python"
if __name__=="__main__":
    pytest.main()