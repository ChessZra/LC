class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        INF = 10 ** 20
        N = len(nums)
        res = 0
        for i in range(N):
            mn, mx = INF, -INF
            for j in range(i, N):
                mn = min(mn, nums[j])
                mx = max(mx, nums[j])
                res += (mx - mn)
        return res