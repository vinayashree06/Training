#Constructor-Student registration, A student's name and roll number must be initialized at object creation. Task: Use a constructor to initialize student details, use unit testing
import unittest
class Student:
    def __init__(self, name, roll_number):
        self.name=name
        self.roll_number=roll_number
class TestStudent(unittest.TestCase):
    def test_student_initialization(self):
        student = Student("Vinaya", 101)
        self.assertEqual(student.name, "Vinaya")
        self.assertEqual(student.roll_number, 101)
        self.assertNotEqual(student.name, "John")
        self.assertNotEqual(student.roll_number, 202)
        
if __name__ == '__main__':
    unittest.main()