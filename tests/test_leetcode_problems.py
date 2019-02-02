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


class BasicTestChecker(unittest.TestCase):
    def test_checker_deck_revealed_increasing(self):
        checker = Array.Checker()
        test_cases = [[2,13,3,11,5,17,7], [1,4,2,6,3,5]]
        for test_case in test_cases:
            self.assertEqual(checker.deckRevealedIncreasing(test_case), sorted(test_case))

class BasicTestSolver(unittest.TestCase):
    def test_checker_deck_revealed_increasing(self):
        solver = Array.Solver()
        checker = Array.Checker()
        test_cases = [[2,13,3,11,5,17,7], [1,4,2,6,3,5]]
        for test_case in test_cases:
            sorted_result = solver.deckRevealedIncreasing(test_case)
            self.assertEqual(checker.deckRevealedIncreasing(sorted_result), sorted(test_case))

if __name__ == '__main__':
    unittest.main()
