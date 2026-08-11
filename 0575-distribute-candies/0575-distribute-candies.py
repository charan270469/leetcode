class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        m = set(candyType)
        n = len(candyType)
        if len(m) < n//2:
            return len(m)
        else:
            return n//2