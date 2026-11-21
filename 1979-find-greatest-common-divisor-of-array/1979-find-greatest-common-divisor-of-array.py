
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mini = min(nums)
        maxi = max(nums)

        while mini != 0:
            rem = maxi % mini
            maxi = mini
            mini = rem

        return maxi
