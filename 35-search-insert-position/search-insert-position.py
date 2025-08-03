class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            for i in range(len(nums)):
                if nums[i] == target:
                    return i
        else:
            for i in range(len(nums)):
                if nums[i] > target:
                    nums.insert(i, target)
                    return i
        nums.append(target)
        return len(nums) - 1
sol = Solution()
sol.searchInsert([1,3,5,6], 5)