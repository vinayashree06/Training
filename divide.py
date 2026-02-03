#divide by zero using unit testing
import unittest

def divide(a,b):
    if b==0:
        raise ValueError("Cannot divide by zero")
    return a/b
class TestDivide(unittest.TestCase):
    def test_divide(self):
        test_cases=[
            (10,2,5),
            (20,4,5),
            (5,0,ValueError),
            (9,3,3)
        ]
        for a,b,result in test_cases:
            with self.subTest(a=a,b=b):
                self.assertEqual(divide(a,b),result)
                       
def test_divide_by_zero(self):
    for b in [0]:
        with self.subTest(b=b):
            self.assertRaises(ValueError,divide,10,b)
if __name__=='__main__':
    unittest.main()