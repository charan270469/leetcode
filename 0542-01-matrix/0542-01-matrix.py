class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])

        q = deque()

        for i in range(n):
            for j in range(m):

                if mat[i][j] == 0:
                    q.append((i,j))
                else:
                    mat[i][j] = -1

        dir = [(0,1),(0,-1),(1,0),(-1,0)]

        while q:

            i,j = q.popleft()

            for r,c in dir:
                mi = i + r
                mj = j + c

                if 0<=mi<n and 0<=mj<m and mat[mi][mj] == -1:
                    mat[mi][mj] = mat[i][j] + 1
                    q.append((mi,mj))
        return mat