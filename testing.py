import unittest
class Widget:
    def __init__(self):
        self.width=50
        self.height=50
    def resize(self,width,height):
        self.width=width
        self.height=height
class WidgetResizeTestCase(unittest.TestCase):
    def test_widget_resize(self):
        widget=Widget()
        self.assertEqual(widget.width,50)
        self.assertEqual(widget.height,50)
def test_widget_resize(self):
    widget=Widget()
    widget.resize(100,150)
    self.assertEqual(widget.width,100)
    self.assertEqual(widget.height,150)

def suite():
    test_suite=unittest.TestSuite()
    test_suite.addTest(WidgetTestCase('test_default_widget_size'))
    test_suite.addTest(WidgetTestCase('test_widget_resize'))
    return suite
if __name__=='__main__':
    runner=unittest.TextTestRunner()
    runner.run(suite())