class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for i in range(31):
            if pow(2,i) == n:
                return True
        else:
            return False
        