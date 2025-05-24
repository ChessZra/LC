class Solution:
    def shortestAlternatingPaths(self, N: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        adj_r = [[] for _ in range(N)]
        for u, v in redEdges:
            adj_r[u].append(v)

        adj_b = [[] for _ in range(N)]
        for u, v in blueEdges:
            adj_b[u].append(v)

        # bfs -> keep track of previous state
        INF = 10 ** 20
        q = deque([(0, 0, 0), (0, 0, 1)]) # index, distance, previous
        distances = [INF] * N
        distances[0] = 0

        visited = set()
        while q:
            n = len(q)

            for i in range(n):
                node, dist, prev_color = q.popleft()

                if (node, prev_color) in visited:
                    continue
                visited.add((node, prev_color))

                if prev_color == 0:
                    for neighbor in adj_r[node]:
                        distances[neighbor] = min(distances[neighbor], 1 + dist)
                        q.append((neighbor, dist + 1, 1))
                else:
                    for neighbor in adj_b[node]:
                        distances[neighbor] = min(distances[neighbor], 1 + dist)
                        q.append((neighbor, dist + 1, 0))

        return [-1 if (x == INF) else x for x in distances]