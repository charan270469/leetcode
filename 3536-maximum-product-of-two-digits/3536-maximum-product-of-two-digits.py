class Solution:
    def maxProduct(self, n: int) -> int:
        m = [int(d) for d in str(n)]

        i = max(m)
        m.remove(i)
        j = max(m)

        return i*j