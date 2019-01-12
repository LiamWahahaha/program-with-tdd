class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}

        for idx, num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target - num], idx]
            else:
                lookup[num] = idx

        return None
