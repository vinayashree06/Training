#suite test
import unittest
class WidgetTestCase(unittest.TestCase):
    def test_default_widget_size(self):
        self.assertEqual(1,1)
    
    def test_widget_resize(self):
        self.assertTrue(True)
def suite():
    suite=unittest.TestSuite()
    suite.addTest(WidgetTestCase('test_default_widget_size'))
    suite.addTest(WidgetTestCase('test_widget_resize'))
    return suite
if __name__=='__main__':
    runner=unittest.TextTestRunner()
    runner.run(suite())