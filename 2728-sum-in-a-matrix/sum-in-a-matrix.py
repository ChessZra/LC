class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        R, C = len(nums), len(nums[0])
        for r in range(R):
            nums[r].sort(reverse=True)
        res = 0
        for c in range(C):
            mx = 0
            for r in range(R):
                mx = max(mx, nums[r][c])
            res += mx
        return res