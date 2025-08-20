class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        in_degree = [0] * n
        for u, v in invocations:
            adj[u].append(v)
            in_degree[v] += 1
        marked = set()
        q = deque([k])
        in_degree_marked = [0] * n
        while q:
            N = len(q)
            for i in range(N):
                cur = q.popleft()
                if cur in marked:
                    continue
                marked.add(cur)
                for neighbor in adj[cur]:
                    in_degree_marked[neighbor] += 1
                    q.append(neighbor)
        valid = True
        for i in range(n):
            if i in marked and in_degree[i] != in_degree_marked[i]:
                valid = False
        if valid:
            res = []
            for i in range(n):
                if i not in marked:
                    res.append(i)
            return res
        return [x for x in range(n)]
