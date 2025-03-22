class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        connected = collections.defaultdict(list)
        visited = set()
        def dfs(node, id):
            if node in visited:
                return
            visited.add(node)
            connected[id].append(node)
            
            for neighbor in adj[node]:
                dfs(neighbor, id)
        
        for i in range(n):
            if i not in visited:
                dfs(i, i)
        
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