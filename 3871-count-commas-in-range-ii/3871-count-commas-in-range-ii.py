class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0

        if n >= 1000:
            ans += min(n, 10**6 - 1) - 1000 + 1

        if n >= 10**6:
            ans += 2 * (min(n, 10**9 - 1) - 10**6 + 1)

        if n >= 10**9:
            ans += 3 * (min(n, 10**12 - 1) - 10**9 + 1)

        if n >= 10**12:
            ans += 4 * (min(n, 10**15 - 1) - 10**12 + 1)

        if n == 10**15:
            ans += 5 * (n - 10**15 + 1)

        return ans