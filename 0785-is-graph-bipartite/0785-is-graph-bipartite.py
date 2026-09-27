class Solution:
    def dfs(self, node, col, color, graph):
        color[node] = col

        for nbr in graph[node]:
            if(color[nbr] == -1):
                if self.dfs(nbr, 1-col, color, graph) == False:
                    return False
            elif(color[nbr] == col):
                return False

        return True

    def isBipartite(self, graph: list[list[int]]) -> bool:
        n = len(graph)

        color = [-1]*n
        
        for i in range(n):
            if(color[i] == -1):
                if self.dfs(i, 0, color, graph) == False:
                    return False
            
        return True
