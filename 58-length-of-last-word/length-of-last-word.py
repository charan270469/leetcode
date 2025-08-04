class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        Words = s.split()
        return len(Words[-1])