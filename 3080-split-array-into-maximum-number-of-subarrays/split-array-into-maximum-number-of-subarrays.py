class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        mn = nums[0]
        N = len(nums)
        for i in range(N):
            mn &= nums[i]
        
        rs = nums[0]
        res = 0
        for i in range(N):
            rs &= nums[i]

            if rs == 0:
                res += 1
                if i < N - 1:
                    rs = nums[i + 1]
        return 1 if res == 0 else res