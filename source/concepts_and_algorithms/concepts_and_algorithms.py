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


    def ugly_number(self, n):
        """
        Ugly numbers are numbers whose only prime factors are 2, 3 or 5.
        """
        i2 = 0
        i3 = 0
        i5 = 0
        ugly = [1]
        next_multiple_of_2 = ugly[i2] * 2
        next_multiple_of_3 = ugly[i3] * 3
        next_multiple_of_5 = ugly[i5] * 5

        for idx in range(1, n):
            ugly.append(min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5))
            if ugly[-1] == next_multiple_of_2:
                i2 += 1
                next_multiple_of_2 = ugly[i2] * 2
            if ugly[-1] == next_multiple_of_3:
                i3 += 1
                next_multiple_of_3 = ugly[i3] * 3
            if ugly[-1] == next_multiple_of_5:
                i5 += 1
                next_multiple_of_5 = ugly[i5] * 5

        return ugly[-1]

class Sort():
    """
    common sorting algorithms
    """

#    def bubble_sort(self, arr):
#        len_of_arr = len(arr)
#
#        for idx_i in range(len_of_arr):
#            for idx_j in range(idx_i + 1, len_of_arr):
#                if arr[idx_i] > arr[idx_j]:
#                    arr[idx_i], arr[idx_j] = arr[idx_j], arr[idx_i]
#
#        return arr

#    def selection_sort(self, arr):
#        len_of_arr = len(arr)
#
#        for idx_i, num in enumerate(arr):
#            minimum = idx_i
#            for idx_j in range(idx_i + 1, len_of_arr):
#                if arr[idx_j] < arr[idx_i]:
#                    minimum = idx_j
#
#            arr[idx_i], arr[minimum] = arr[minimum], arr[idx_i]
#
#        return arr

