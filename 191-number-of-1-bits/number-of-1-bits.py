class Solution:
    def hammingWeight(self, n: int) -> int:
        m = bin(n)
        x = list(m[2:])
        count = 0
        for i in x:
            if i == '1':
                count = count + 1
        return count