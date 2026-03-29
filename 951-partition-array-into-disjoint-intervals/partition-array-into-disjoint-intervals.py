class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        INF = 10 ** 20
        lmx = -INF
        rmn = INF
        N = len(nums)
        right = [None] * N
        for i in range(N - 1, 0, -1):
            rmn = min(rmn, nums[i])
            right[i] = rmn
        for i in range(N - 1):
            lmx = max(lmx, nums[i])
            if lmx <= right[i + 1]:
                return i + 1
        return -1