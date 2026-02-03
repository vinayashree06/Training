import unittest
class TestStringLength(unittest.TestCase):
    def test_string_length(self):
        strings={
            "apple":5,
            "banana":8,
            "cat":3,
            "vinaya":8
        }
        for text,length in strings.items():
            with self.subTest(string=text):
                self.assertEqual(len(text),length)
if __name__=='__main__':
    unittest.main()
        