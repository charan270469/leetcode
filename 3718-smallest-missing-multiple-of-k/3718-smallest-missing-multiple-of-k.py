class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        n =0
        if len(nums) < 2:
            if nums[0] == k:
                return k+k
            else:
                return k
        for i in range(len(nums)):
            n += k
            if n not in nums:
                return n
        return n+k
