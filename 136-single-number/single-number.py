class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0)+1
        for i in nums:
            if freq[i] == 1:
                return i