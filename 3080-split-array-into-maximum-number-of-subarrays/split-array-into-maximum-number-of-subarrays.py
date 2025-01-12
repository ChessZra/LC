class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        N = len(nums)
        rs = nums[0]
        res = 0
        for i in range(N):
            rs &= nums[i]
            if rs == 0:
                res += 1
                if i < N - 1:
                    rs = nums[i + 1]
        return 1 if res == 0 else res