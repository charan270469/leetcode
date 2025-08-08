class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            num = sum(int(x) for x in str(num))
        return num

