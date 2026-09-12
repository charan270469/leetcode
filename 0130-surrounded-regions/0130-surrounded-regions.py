class Solution:
    def dfs(self, board, vis, r, c ):
        vis[r][c] = 1

        n = len(board)
        m = len(board[0])

        dir = [(0,1),(0,-1),(1,0),(-1,0)]

        for dr,dc in dir:
            nr = r + dr
            nc = c + dc

            if 0<=nr<n and 0<=nc<m and vis[nr][nc] == 0 and board[nr][nc] == "O":
                self.dfs(board, vis, nr, nc)

    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])

        vis = [[0]*m for _ in range(n)]

        for j in range(m):
            if board[0][j] == "O":
                self.dfs(board, vis, 0, j)
            if board[n-1][j] == "O":
                self.dfs(board, vis, n-1, j)

        for i in range(n):
            if board[i][0] == "O":
                self.dfs(board,vis,i,0)
            if board[i][m-1] == "O":
                self.dfs(board, vis, i, m-1)

        for i in range(n):
            for j in range(m):
                if board[i][j] == "O" and vis[i][j] == 0:
                    board[i][j] = "X"