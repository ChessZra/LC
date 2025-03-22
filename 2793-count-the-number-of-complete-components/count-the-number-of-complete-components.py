class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        connected = collections.defaultdict(list)
        seen = [False] * n
        def bfs(node, id):
            q = deque([node])
            while q:
                cur = q.popleft()
                if seen[cur]: continue
                seen[cur] = True
                connected[id].append(cur)

                for neighbor in adj[cur]:
                    q.append(neighbor)

        for i in range(n):
            if not seen[i]:
                bfs(i, i)

        res = 0
        for id, nodes in connected.items():
            num_nodes = len(nodes)
            valid = True
            for node in nodes:
                if len(adj[node]) != num_nodes - 1:
                    valid = False
                    break
            res += int(valid)
        return res