class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(c + 1)]
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)
        components = {}
        ids = {}
        visited = [False] * (c + 1)
        def dfs(node, id):
            if visited[node]:
                return
            visited[node] = True
            if id not in components:
                components[id] = [] # initialize min heap
            heapq.heappush(components[id], node)
            ids[node] = id
            for nxt in adj[node]:
                dfs(nxt, id)
        for node in range(1, c + 1):
            if not visited[node]:
                dfs(node, node)
        offline = set()
        res = []
        for op, x in queries:
            if op == 2:
                offline.add(x)
            else: # op = 3
                # print(f'for node {x}, list is {components[ids[x]]}')
                while components[ids[x]] and components[ids[x]][0] in offline:
                    heappop(components[ids[x]])
                if not components[ids[x]]:
                    res.append(-1)
                elif x not in offline:
                    res.append(x)
                else:
                    res.append(components[ids[x]][0])
        return res

        
