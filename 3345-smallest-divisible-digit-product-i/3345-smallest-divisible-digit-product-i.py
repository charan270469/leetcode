class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        i = n
        while i:
            m = [int(d) for d in str(i)]

            if math.prod(m) % t == 0:
                return i
            else:
                i+=1
        return 