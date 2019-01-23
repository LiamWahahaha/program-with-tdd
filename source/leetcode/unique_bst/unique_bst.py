class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        g = [0] * (n + 1)
        g[0] = 1
        g[1] = 1

        for idx_n in range(2, n + 1):
            for idx_i in range(1, idx_n + 1):
                g[idx_n] += g[idx_i - 1] * g[idx_n - idx_i]

        return g[n]
