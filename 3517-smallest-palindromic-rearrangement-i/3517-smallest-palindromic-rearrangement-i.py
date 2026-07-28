class Solution:
    def smallestPalindrome(self, s: str) -> str:
        c = Counter(s)

        left = []
        mid = ""

        for ch in sorted(c):
            left.append(ch * (c[ch] // 2))
            if c[ch] % 2:
                mid = ch

        left = "".join(left)
        return left + mid + left[::-1]