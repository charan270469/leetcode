class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = {}

        for i in s:
            count[i] = count.get(i, 0) + 1

        for i in t:
            if i not in count or count[i] == 0:
                return i
            count[i] -= 1