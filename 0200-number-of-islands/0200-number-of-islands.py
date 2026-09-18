class Solution:
    def dfs(self, grid, vis, r, c):
        n = len(grid)
        m = len(grid[0])

        vis[r][c] = 1

        dir = [(1,0),(-1,0),(0,1),(0,-1)]

        for dr,dc in dir:
            nr = r + dr
            nc = c + dc

            
            if 0<=nr<n and 0<=nc<m and grid[nr][nc]== "1" and vis[nr][nc]!=1:
                self.dfs(grid, vis, nr, nc)

    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        vis = [[0]*m for i in range(n)]

        islands = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and vis[i][j]!=1:
                    self.dfs(grid, vis, i, j)
                    islands += 1

        return islands