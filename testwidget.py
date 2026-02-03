import unittest

from matplotlib.widgets import Widget
class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget=Widget('the widget')
    def tearDown(self):
        self.widget.dispose()
if __name__=='__main__':
    unittest.main()