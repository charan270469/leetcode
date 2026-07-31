class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = set(nums2)
        ans = []

        for x in set(nums1):
            if x in s:
                ans.append(x)

        return ans