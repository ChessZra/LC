class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        visited = [[False] * C for _ in range(R)]
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        ans = 0
        size = 0
        def dfs(r, c):
            if visited[r][c]:
                return
            if grid[r][c] == 0:
                return

            visited[r][c] = True
            nonlocal ans, size
            size += 1
            ans = max(ans, size)
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C:
                    dfs(nr, nc)
        
        for r in range(R):
            for c in range(C):
                if not visited[r][c]:
                    dfs(r, c)
                    size = 0 # reset
        return ans