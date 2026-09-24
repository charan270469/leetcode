class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 10 and nums[i] == i:
                return i
            else:
                isum = 0
                for ch in str(nums[i]):
                    isum += int(ch)
                if isum == i:
                    return i
        return -1