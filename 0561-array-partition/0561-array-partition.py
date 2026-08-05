class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        i = 0
        optsum = 0
        while i < len(nums):
            optsum += min(nums[i],nums[i+1])
            i = i + 2
        return optsum