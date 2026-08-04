class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        i = min(nums)
        j = max(nums)
        res = []

        while i != j:
            if i not in nums:
                res.append(i)
            i += 1
        
        return res