class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        ct = 0
        for ch in patterns:
            if ch in word:
                ct += 1
        return ct