class Solution:
    def countEven(self, num: int) -> int:
        res = []
        for i in range(1,num+1):
            if i < 10 and i % 2 == 0:
                res.append(i)
            else:
                m = list(map(int, str(i)))
                if sum(m) % 2 == 0:
                    res.append(i)
        return len(res)