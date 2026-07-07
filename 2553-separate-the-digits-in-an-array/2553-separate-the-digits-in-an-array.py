class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        s = "".join(map(str,nums))
        n = [int(ch) for ch in s]

        return n