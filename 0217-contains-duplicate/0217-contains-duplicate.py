class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        nodup = set(nums)
        m = len(nodup)

        return n != m