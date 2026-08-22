class Solution:
    def checkDivisibility(self, n: int) -> bool:
        k = n
        s = 0
        m = 1
        lst = list(map(int, str(n)))
        for i in lst:
            s = s+i
            m = m*i
        return k%(s+m) == 0