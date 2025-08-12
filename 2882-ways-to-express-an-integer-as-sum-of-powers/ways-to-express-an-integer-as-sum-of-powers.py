class Solution:
    def numberOfWays(self, N: int, x: int) -> int:
        # MOD = 10 ** 9 + 7

        # @cache
        # def solve(current, n):
        #     if n == N:
        #         return 1
        #     if n > N or current > N:
        #         return 0
        #     yes = solve(current + 1, n + current ** x)
        #     no = solve(current + 1, n)
        #     return (yes + no) % MOD

        # solve.cache_clear()
        # return solve(1, 0)
        MOD = 10**9 + 7

        # Precompute powers to avoid repeated calculation
        powers = [i**x for i in range(N+1)]

        # dp[i][j]: number of ways to reach sum j using numbers from i..N
        dp = [[0]*(N+1) for _ in range(N+2)]  # N+2 rows to handle dp[N+1][*]

        # Base case: if sum == N, exactly 1 way (we reached target)
        for i in range(N+2):
            dp[i][N] = 1

        # Fill table bottom-up
        for current in range(N, 0, -1):
            for n in range(N+1):
                no = dp[current+1][n]  # skip current number
                yes = 0
                nxt = n + powers[current]
                if nxt <= N:
                    yes = dp[current+1][nxt]  # include current number
                dp[current][n] = (yes + no) % MOD

        return dp[1][0]