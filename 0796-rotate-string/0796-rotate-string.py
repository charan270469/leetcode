class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            i = i % len(s)
            ns = s[-i:] + s[:-i]
            if ns == goal:
                return True
        return False