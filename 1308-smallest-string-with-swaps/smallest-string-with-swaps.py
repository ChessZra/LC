class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        adj = collections.defaultdict(list)

        for u, v in pairs:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        union = collections.defaultdict(list)
        def dfs(index, identifier):
            if index in visited:
                return
            
            visited.add(index)
            union[identifier].append(index)
            for nxt in adj[index]:
                dfs(nxt, identifier)
        
        for index, char in enumerate(s):
            if index not in visited:
                dfs(index, index)
        
        heaps = {}
        index_to_id = {}

        for k, v in union.items():
            heaps[k] = [] # initialize heap for this id

            for index in v:
                heappush(heaps[k], ord(s[index]))
                index_to_id[index] = k

        res = ""
        for index in range(len(s)):
            identifier = index_to_id[index]
            res += chr(heappop(heaps[identifier]))

        return res