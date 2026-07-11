class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        streak = 0
        res = 2
        for i in range(2, N):
            if nums[i] == (nums[i - 1] + nums[i - 2]):
                streak += 1
                res = max(res, streak + 2)
            else:
                streak = 0
        return res