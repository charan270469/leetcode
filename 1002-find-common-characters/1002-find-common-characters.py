
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = [100] * 26

        for word in words:
            freq = [0] * 26

            for ch in word:
                freq[ord(ch) - ord('a')] += 1

            for i in range(26):
                common[i] = min(common[i], freq[i])

        result = []

        for i in range(26):
            for _ in range(common[i]):
                result.append(chr(i + ord('a')))

        return result
