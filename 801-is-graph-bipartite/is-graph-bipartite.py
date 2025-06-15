class Solution:
    def isBipartite(self, adj: List[List[int]]) -> bool:
        N = len(adj)
        colors = [-1] * N
        
        visited = [False] * N
        def dfs(node, color):
            if visited[node]:
                return
            
            visited[node] = True
            colors[node] = color
            for neighbor in adj[node]:
                dfs(neighbor, 1 - color)

        for i in range(N):
            if not visited[i]:
                dfs(i, 0)

        for u in range(N):
            for v in adj[u]:
                if colors[u] == colors[v]:
                    return False
        return True