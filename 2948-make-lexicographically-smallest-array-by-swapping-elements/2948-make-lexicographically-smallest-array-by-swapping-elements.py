class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)

        # Store (value, original_index)
        arr = sorted((nums[i], i) for i in range(n))

        ans = nums[:]

        l = 0

        while l < n:
            r = l

            # Find all values belonging to the same group
            while r + 1 < n and arr[r + 1][0] - arr[r][0] <= limit:
                r += 1

            # Values are already sorted
            vals = [arr[i][0] for i in range(l, r + 1)]

            # Get their original indices and sort them
            idx = sorted(arr[i][1] for i in range(l, r + 1))

            # Put smallest values at smallest indices
            for i in range(len(vals)):
                ans[idx[i]] = vals[i]

            l = r + 1

        return ans