class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        q = deque()
        fresh = 0

        for r in range(n):
            for c in range(m):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        tm = 0
        dir = [[1,0],[-1,0],[0,1],[0,-1]]

        while q and fresh > 0:

            for i in range(len(q)):
                r,c = q.popleft()

                for dr, dc in dir:
                    nr = r + dr
                    nc = c + dc
                    
                    if 0 <= nr < n and 0 <= nc < m:
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            q.append((nr,nc))
                            fresh -= 1

            tm += 1

        if fresh > 0:
            return -1
        return tm