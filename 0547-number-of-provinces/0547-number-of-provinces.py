from collections import deque
from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [False] * len(isConnected)
        comps = 0

        for i in range(len(isConnected)):

            # Start BFS only if this city is not visited
            if not visited[i]:
                comps += 1

                q = deque()
                q.append(i)
                visited[i] = True

                while q:
                    node = q.popleft()

                    # Check every possible city
                    for nbr in range(len(isConnected)):
                        if isConnected[node][nbr] == 1 and not visited[nbr]:
                            visited[nbr] = True
                            q.append(nbr)

        return comps