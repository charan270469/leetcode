class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [
            set("qwertyuiop"),
            set("asdfghjkl"),
            set("zxcvbnm")
        ]

        ans = []

        for word in words:
            s = set(word.lower())
            for row in rows:
                if s <= row:      # all letters are in this row
                    ans.append(word)
                    break

        return ans