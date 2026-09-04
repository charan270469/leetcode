class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n = len(image)
        m = len(image[0])

        original = image[sr][sc]

        if original == color:
            return image

        q = deque()
        q.append((sr,sc))

        image[sr][sc] = color


        dir = [[1,0],[-1,0],[0,1],[0,-1]]

        while q:
            sr,sc = q.popleft()
                
            for r,c in dir:
                nr = sr + r
                nc = sc + c

                if 0<=nr<n and 0<=nc<m:
                    if image[nr][nc] == original:
                        image[nr][nc] = color

                        q.append((nr,nc))
        return image