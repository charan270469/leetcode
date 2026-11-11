class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        rh = sorted(heights)
        ct = 0
        for i in range(len(heights)):
            if heights[i] != rh[i]:
                ct += 1
        return ct