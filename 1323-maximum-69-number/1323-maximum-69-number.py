class Solution:
    def maximum69Number(self, num: int) -> int:
        m = [int(d) for d in str(num)]

        if 6 in m:
            i = m.index(6)
            m[i] = 9

        n = int(''.join(map(str, m)))
        return n