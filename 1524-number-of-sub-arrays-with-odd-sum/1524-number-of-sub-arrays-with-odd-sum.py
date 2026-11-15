
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7

        even = 1  # Empty prefix sum is even
        odd = 0
        prefix_sum = 0
        result = 0

        for num in arr:
            prefix_sum += num

            if prefix_sum % 2 == 0:
                result += odd
                even += 1
            else:
                result += even
                odd += 1

        return result % MOD
