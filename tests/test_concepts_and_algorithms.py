import unittest

from .context import Concepts


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_triple_step(self):
        for example in [Concepts.Recursion(), Concepts.DP()]:
            self.assertEqual(example.triple_step(3), 4)
            self.assertEqual(example.triple_step(4), 7)


if __name__ == '__main__':
    unittest.main()
