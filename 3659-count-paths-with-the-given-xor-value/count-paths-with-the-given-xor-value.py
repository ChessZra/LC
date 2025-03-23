class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        R, C = len(grid), len(grid[0])
        MOD = 10 ** 9 + 7
        dp = [[[None] * 16 for _ in range(C + 1)] for _ in range(R + 1)]

        for r in range(R - 1, -1, -1):
            for c in range(C - 1, -1, -1):
                for cur in range(16):

                    if r == R - 1 and c == C - 1:
                        dp[r][c][cur] = int(cur == k)
                        continue
                    
                    total = 0
                    if c + 1 < C:
                        total += dp[r][c + 1][cur ^ grid[r][c + 1]]
                    if r + 1 < R:
                        total += dp[r + 1][c][cur ^ grid[r + 1][c]]
                    total %= MOD
                    dp[r][c][cur] = total 
                    
        return dp[0][0][grid[r][c]]

        """
        cache = {}
        def solve(r, c, cur):
            if r == R - 1 and c == C - 1:
                return 1 if cur == k else 0
            
            if (r, c, cur) in cache:
                return cache[(r, c, cur)]

            total = 0
            # right
            if c + 1 < C:
                total += solve(r, c + 1, cur ^ grid[r][c + 1])
            
            # down
            if r + 1 < R:
                total += solve(r + 1, c, cur ^ grid[r + 1][c])
            
            cache[(r, c, cur)] = total

            return total
        return solve(0, 0, grid[0][0]) % MOD
        """