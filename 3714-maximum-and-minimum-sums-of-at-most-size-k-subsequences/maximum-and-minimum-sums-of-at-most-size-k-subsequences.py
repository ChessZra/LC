import math

class Solution:
    def minMaxSums(self, nums: List[int], k: int) -> int:
        nums.sort()
        N = len(nums)
        res = 0
        MOD = 10 ** 9 + 7

        def precompute_binomial(n, k, MOD):
            C = [[0] * (k + 1) for _ in range(n + 1)]
            for i in range(n + 1):
                C[i][0] = 1
                for j in range(1, min(i, k) + 1):
                    C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD
            return C

        choose = precompute_binomial(N, k, MOD)

        for i in range(N):
            res += nums[i]
            for j in range(1, min(k, N - i)):
                res += choose[N - i - 1][j] * nums[i] 
                res %= MOD

        for i in range(N - 1, -1, -1):
            res += nums[i]
            for j in range(1, min(k, i + 1)):
                res += choose[i][j] * nums[i]
                res %= MOD

        return res % MOD