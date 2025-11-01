class Solution:
    def countPairs(self, N: int, edges: List[List[int]]) -> int:
        """
        1 2 4
        6 8 0 = 14
        """
        adj = [[] for _ in range(N)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        comp = collections.Counter()
        visited = [False] * N
        def dfs(node, id):
            if visited[node]:
                return
            visited[node] = True
            comp[id] += 1
            for nxt in adj[node]:
                dfs(nxt, id)
        for i in range(N):
            if not visited[i]:
                dfs(i, i)
        arr = list(comp.values())
        res = 0
        rs = 0
        for i in range(len(arr) - 1, -1, -1):
            res += rs * arr[i]
            rs += arr[i]
        return res