class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for x in nums:
            res += [subset + [x] for subset in res]

        return res