class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)

        for i in range(n):
            while nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i in range(n):
            if nums[i] != i + 1:
                return [nums[i], i + 1]