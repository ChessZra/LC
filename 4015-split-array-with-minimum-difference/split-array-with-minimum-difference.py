class Solution:
    def splitArray(self, nums: List[int]) -> int:
        INF = 10 ** 20
        res = INF
        N = len(nums)
        bad = -1
        for i in range(N - 2, -1, -1):
            if nums[i + 1] >= nums[i]:
                bad = i
                break
        right_sum = [None] * N
        s = 0
        for i in range(N - 1, -1, -1):
            s += nums[i]
            right_sum[i] = s
        s = 0
        for i in range(N - 1):
            s += nums[i]
            if i > 0 and nums[i] <= nums[i - 1]:
                break
            if i >= bad:
                # print('here', s, i)
                res = min(res, abs(s - right_sum[i + 1]))
        # print(bad, right_sum)
        return -1 if res == INF else res