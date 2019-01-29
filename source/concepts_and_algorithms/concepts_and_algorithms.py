class Recursion():
    """
    Some recursion example
    """

    def triple_step(self, n):
        """
        question 8.1
        A child is running up a staircase with n steps and can hop either 1 step,
        2 steps, or 3 steps at a time.
        """
        if n == 0:
            return 1
        elif n <= 2:
            return n
        else:
            return self.triple_step(n - 1) + \
                   self.triple_step(n - 2) + \
                   self.triple_step(n - 3)

class DP():
    """
    Some dynamic programming examples
    """

    def triple_step(self, n):
        """
        question 8.1
        A child is running up a staircase with n steps and can hop either 1 step,
        2 steps, or 3 steps at a time.
        """
        if n <= 2:
            return n
        hop = [0 for _ in range(n + 1)]
        hop[0] = 1
        hop[1] = 1
        hop[2] = 2

        for idx in range(3, n + 1):
            hop[idx] = hop[idx - 1] + hop[idx - 2] + hop[idx - 3]

        return hop[n]
