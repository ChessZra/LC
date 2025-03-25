class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        N = len(arr)
        res = []
        dp = []
        running_xor = [0] * 32
        for num in arr:
            for i in range(32):
                if (num & (1 << i)) > 0:
                    running_xor[i] += 1
            dp.append(tuple(running_xor))

        for left, right in queries:
            bit = [dp[right][i] - (0 if left == 0 else dp[left - 1][i]) for i in range(32)]
            n = 0
            for i in range(32):
                if bit[i] % 2 == 1:
                    n += (1 << i)
            res.append(n)

        return res
