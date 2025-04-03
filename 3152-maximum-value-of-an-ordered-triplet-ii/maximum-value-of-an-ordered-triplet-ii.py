class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        N = len(nums)
        prefix = [[0, 0] for _ in range(N)] 
        suffix = [[0, 0] for _ in range(N)]
        mx, mn = 0, 0
        for i in range(N):
            mx = max(mx, nums[i])
            prefix[i][0] = mn
            prefix[i][1] = mx
            mn = min(mn, nums[i])
        mx, mn = 0, 0
        for i in range(N - 1, -1, -1):
            suffix[i][0] = mn
            suffix[i][1] = mx
            mx = max(mx, nums[i])
            mn = min(mn, nums[i])
        res = 0
        for i in range(1, N - 1):
            res = max(res, (prefix[i][1] - nums[i]) * suffix[i][1])
        return res