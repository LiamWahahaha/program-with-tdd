from collections import deque as dq

class Solver():

    def deckRevealedIncreasing(self, arr):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        len_of_deck = len(arr)
        idx = dq(range(len_of_deck))
        ans = [None] * len_of_deck

        for card in sorted(arr):
            ans[idx.popleft()] = card
            if idx:
                idx.append(idx.popleft())

        return list(ans)

class Checker():
    def deckRevealedIncreasing(self, arr):
        ret_arr = []
        queue = dq(arr)

        while queue:
            ret_arr.append(queue.popleft())
            if queue:
                val = queue.popleft()
                queue.append(val)

        return ret_arr
