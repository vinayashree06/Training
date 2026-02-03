#unit testing to check float values
import unittest
class FloatTestCase(unittest.TestCase):
    def test_float(self):
        float_value = 5
        self.assertIsInstance(float_value, float)
if __name__ == '__main__':
    unittest.main()