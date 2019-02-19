import unittest

from .context import Concepts


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_triple_step(self):
        for example in [Concepts.Recursion(), Concepts.DP()]:
            self.assertEqual(example.triple_step(3), 4)
            self.assertEqual(example.triple_step(4), 7)

    def test_ugly_number(self):
        dp = Concepts.DP()
        self.assertEqual(dp.ugly_number(7), 8)
        self.assertEqual(dp.ugly_number(10), 12)
        self.assertEqual(dp.ugly_number(15), 24)
        self.assertEqual(dp.ugly_number(150), 5832)

    def test_bubble_sort(self):
        sort = Concepts.Sort()
        testcases = [[5,23,1,5,0], [123,5,7,9], [-10, 982,42,8]]

        for testcase in testcases:
            self.assertEqual(sort.bubble_sort(testcase), sorted(testcase))

    def test_selection_sort(self):
        sort = Concepts.Sort()
        testcases = [[5,23,1,5,0], [123,5,7,9], [-10, 982,42,8]]

        for testcase in testcases:
            self.assertEqual(sort.selection_sort(testcase), sorted(testcase))

if __name__ == '__main__':
    unittest.main()
