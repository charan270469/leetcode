class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p = 1
        s = 0
        while n > 0:

            r = n % 10
            n = n // 10

            p = p*r
            s = s+r
                
        return p - s