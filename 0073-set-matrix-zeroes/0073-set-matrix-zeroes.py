from collections import deque

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])

        q = deque()

        # Store positions of original zeroes
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    q.append((i, j))

        # Set corresponding rows and columns to zero
        while q:
            r, c = q.popleft()

            for i in range(n):
                matrix[i][c] = 0

            for j in range(m):
                matrix[r][j] = 0