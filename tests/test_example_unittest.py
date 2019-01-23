import unittest

from .context import *

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_hello_world(self):
        self.assertEqual(hello_world(), 'hello world')

if __name__ == '__main__':
    unittest.main()
