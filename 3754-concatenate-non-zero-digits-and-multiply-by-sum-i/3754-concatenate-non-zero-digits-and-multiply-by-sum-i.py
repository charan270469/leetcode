class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = str(n)
        a = 0
        m = ""

        for i in range(len(s)):
            if s[i] != "0":
                m += s[i]
                a += int(s[i])

        if m == "":
            return 0
        k = int(m)
        return k*a


