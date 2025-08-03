class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join(map(str, digits)))
        num = num + 1
        final = [int(d) for d in str(num)]
        return final
sol = Solution()
sol.plusOne([1,2,3])