class Solution:
    def rob(self, nums: list[int]) -> int:
        r1 = 0
        r2 = 0

        for i in nums:
            temp = max(i+r1,r2)
            r1 = r2
            r2 = temp
        return r2