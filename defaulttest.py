import unittest
class Widget:
    def __init__(self, name):
        self.name=name
    def size(self):
        return (50,50)
class DefaultWidgetSizeTestCase(unittest.TestCase):
    def test_default_size(self):
        widget=Widget('the widget')
        self.assertEqual(widget.size(), (50,50))
if __name__=='__main__':
    unittest.main()