class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        res = 0
        char_count = Counter(chars)

        for word in words:
            word_count = Counter(word)

            if all(word_count[c] <= char_count[c] for c in word_count):
                res += len(word)

        return res