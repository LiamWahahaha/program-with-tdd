import unittest

from .context import *

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_two_sum(self):
        two_sum = TwoSum.Solution()
        self.assertEqual(two_sum.twoSum([2, 7, 11, 15], 9), [0, 1])

    def test_unique_bst(self):
        unique_bst = UniqueBST.Solution()
        self.assertEqual(unique_bst.numTrees(3), 5)

if __name__ == '__main__':
    unittest.main()
