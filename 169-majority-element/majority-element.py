class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        counter = Counter(nums)
        most_common = counter.most_common(1)[0][0]
        return most_common
