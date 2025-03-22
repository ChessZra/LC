class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        
        count = []
        for c in range(C):
            f = collections.Counter()
            for r in range(R):
                f[grid[r][c]] += 1
            count.append(f)

        INF = float('inf')
        @cache
        def solve(c, prev):
            if c == C:
                return 0

            ans = INF
            for i in range(10):
                if i == prev:
                    continue
                ans = min(ans, R - count[c][i] + solve(c + 1, i))
            return ans
        
        return solve(0, -1)