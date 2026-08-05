class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        optsum = 0
        for i in range(0,len(nums),2):
            optsum+=nums[i]
        return optsum