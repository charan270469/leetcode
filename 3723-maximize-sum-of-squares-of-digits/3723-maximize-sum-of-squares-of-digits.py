
class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""

        ans = []

        for i in range(num):
            digit = min(9, sum)
            ans.append(str(digit))
            sum -= digit

        return "".join(ans)
