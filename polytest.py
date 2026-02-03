#You are given a base class Shape, Different shapes calculate area differently, Task: Override the area() method in each subclass, use unit testing
import unittest
class Shape:
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius 
class TestShapeArea(unittest.TestCase):
    def test_rectangle_area(self):
        rect=Rectangle(4,5)
        self.assertEqual(rect.area(),20)
    def test_circle_area(self):
        circ=Circle(3)
        self.assertAlmostEqual(circ.area(),28.26)   
if __name__=='__main__':
    unittest.main()