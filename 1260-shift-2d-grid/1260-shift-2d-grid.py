from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        total = m * n
        k = k % total

        ans = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                # Current position in 1D
                pos = i * n + j

                # New position after shifting
                new_pos = (pos + k) % total

                # Convert back to 2D indices
                new_i = new_pos // n
                new_j = new_pos % n

                ans[new_i][new_j] = grid[i][j]

        return ans