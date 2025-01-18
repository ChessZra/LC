class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        N = len(parents)
        adj = [[] for _ in range(N)]

        # Create the tree from parents
        for i in range(1, N):
            adj[parents[i]].append(i)

        @cache
        def get_size(node):
            sz = 1
            for c in adj[node]:
                sz += get_size(c)
            return sz

        f = collections.Counter() # score: frequency
        def dfs(node):
            if node is None:
                return
            
            prod = 1
            total = 0
            for c in adj[node]:
                total += get_size(c)
                prod *= get_size(c)
                dfs(c) # try out other stuff

            prod *= max(1, N - 1 - total)
            f[prod] += 1
            
        dfs(0)

        return f[max(f.keys())]