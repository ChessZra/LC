class Solution:
    def maxWeight(self, n: int, edges: List[List[int]], k: int, t: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
        
        @cache
        def solve(node, k, weight):
            if weight >= t:
                return -1
            if k == 0:
                return weight
            
            res = -1
            for v, w in adj[node]:
                res = max(res, solve(v, k - 1, weight + w))
            return res
        
        best = -1
        for i in range(n):
            best = max(best, solve(i, k, 0))
        return best