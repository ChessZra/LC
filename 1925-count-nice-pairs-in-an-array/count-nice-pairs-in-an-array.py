class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        N = len(nums)
        revs = {}
        for i in range(N):
            revs[nums[i]] = int(str(nums[i])[::-1])
        f = collections.Counter()
        res = 0
        for i in range(N):
            # 97 + 24 = 79 + 42
            res += f[nums[i] - revs[nums[i]]]
            res %= MOD
            f[nums[i] - revs[nums[i]]] += 1
        return res