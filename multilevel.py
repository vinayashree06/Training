#Multilevel inheritance unit testing
import unittest
class Grandparent:
    def get_grandparent_name(self):
        return "Grandparent Name"
class Parent(Grandparent):
    def get_parent_name(self):
        return "Parent Name"    
class Child(Parent):
    def get_child_name(self):
        return "Child Name"
class TestMultilevelInheritance(unittest.TestCase):
    def test_grandparent_name(self):
        grandparent = Grandparent()
        self.assertEqual(grandparent.get_grandparent_name(), "Grandparent Name")
    def test_parent_name(self):
        parent = Parent()
        self.assertEqual(parent.get_parent_name(), "Parent Name")
    def test_child_name(self):
        child = Child()
        self.assertEqual(child.get_child_name(), "Child Name")
if __name__ == '__main__':
    unittest.main()