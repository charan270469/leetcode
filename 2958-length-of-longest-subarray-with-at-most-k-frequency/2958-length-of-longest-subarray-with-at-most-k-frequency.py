class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        count = {}
        ans = 0
        left = 0

        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i],0)+1

            while count[nums[i]] > k:
                count[nums[left]] -= 1
                left += 1

            ans = max(ans, i - left + 1)
        return ans