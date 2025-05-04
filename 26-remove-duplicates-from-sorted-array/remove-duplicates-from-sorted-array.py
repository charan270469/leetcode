class Solution(object):
    def removeDuplicates(self, nums):
        nums[:] = list(dict.fromkeys(nums))
        nums.sort()
        return len(nums)
        
s = Solution()
k = s.removeDuplicates([1,1,2])