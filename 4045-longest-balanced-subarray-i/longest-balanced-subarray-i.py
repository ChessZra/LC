class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        N = len(nums)
        best = 0
        for i in range(N):
            odds, evens = {}, {}
            for j in range(i, N):
                if nums[j] % 2 == 0:
                    evens[nums[j]] = 1 + evens.get(nums[j], 0)
                else:
                    odds[nums[j]] = 1 + odds.get(nums[j], 0)
                if len(odds) == len(evens):
                    best = max(best, j - i + 1)
        return best