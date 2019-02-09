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

if __name__ == '__main__':
    unittest.main()
