class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        N = len(nums)
        f = collections.Counter()
        res = 0
        for i in range(N):
            # 97 + 24 = 79 + 42
            rev = int(str(nums[i])[::-1])
            res += f[nums[i] - rev]
            res %= MOD
            f[nums[i] - rev] += 1
        return res