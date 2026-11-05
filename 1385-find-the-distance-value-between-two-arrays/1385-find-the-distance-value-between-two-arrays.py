class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        count = 0

        for num in arr1:
            valid = True

            for n in arr2:
                if abs(num - n) <= d:
                    valid = False
                    break

            if valid:
                count += 1

        return count