class Solution:
    def isHappy(self, n: int) -> bool:
        sq = set()
        while n != 1 and n not in sq:
            sq.add(n)
            n = sum(int(d)**2 for d in str(n))
        return n == 1