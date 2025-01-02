class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        N = len(patience)
        INF = 10 ** 20
        adj = [[] for _ in range(N)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        pq = [(0, 0)]
        distances = [INF] * N
        distances[0] = 0
        visited = set()
        while pq:
            time, server = heappop(pq)

            if server in visited:
                continue
            visited.add(server)

            for neighbor in adj[server]: 
                if time + 1 <= distances[neighbor]:
                    distances[neighbor] = time + 1
                    heappush(pq, (time + 1, neighbor))
        
        res = 0
        for server, dist in enumerate(distances):
            if server == 0: continue
            sent = (dist * 2 - 1) // patience[server]
            takes = (sent * patience[server]) + (dist * 2)
            res = max(res, takes)
        return res + 1