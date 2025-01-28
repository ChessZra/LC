class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visited = [[False] * C for _ in range(R)]

        f = collections.Counter()
        def dfs(r, c, ide):
            if visited[r][c] or grid[r][c] == 0:
                return
            
            visited[r][c] = True
            f[ide] += grid[r][c]
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < R and 0 <= nc < C:
                    dfs(nr, nc, ide)

        for r in range(R):
            for c in range(C):
                if not visited[r][c]:
                    dfs(r, c, (r, c))
        if not f.values():
            return 0
        return max(f.values()) 