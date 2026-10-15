from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        sqsums = 0

        for i in range(n):
            for j in range(i, n):
                distinct = len(set(nums[i:j+1]))
                sqsums += distinct ** 2

        return sqsums