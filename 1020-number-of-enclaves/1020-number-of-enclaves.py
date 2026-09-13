class Solution:
    def dfs(self, grid, vis, r, c):
        vis[r][c] = 1

        n = len(grid)
        m = len(grid[0])

        dir = [(1,0),(-1,0),(0,1),(0,-1)]

        for dr,dc in dir:
            nr = r + dr
            nc = c + dc

            if 0<=nr<n and 0<=nc<m and grid[nr][nc] == 1 and vis[nr][nc] == 0:
                self.dfs(grid, vis, nr, nc)

    def numEnclaves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        vis = [[0]*m for _ in range(n)]

        if n == 0 or m == 0:
            return

        for j in range(m):
            if grid[0][j] == 1:
                self.dfs(grid, vis, 0, j)
            if grid[n-1][j] == 1:
                self.dfs(grid, vis, n-1, j)
        
        for i in range(n):
            if grid[i][0] == 1:
                self.dfs(grid, vis, i, 0)
            if grid[i][m-1] == 1:
                self.dfs(grid, vis, i, m-1)
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and vis[i][j] == 0:
                    count += 1
        
        return count
        