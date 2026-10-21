class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        return nums.index(max(nums))