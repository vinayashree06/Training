import unittest
def square(n):
    return n*n
class TestSquare(unittest.TestCase):
    def test_square(self):
        test_data=[
            (2,4),
            (3,10),
            (4,16),
            (5,25)
        ]
        for num,expected in test_data:
            with self.subTest(num=num):
                self.assertEqual(square(num),expected)
if __name__=='__main__':
    unittest.main()