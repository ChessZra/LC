class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        R, C = len(grid), len(grid[0])
        nums = []
        is_possible = grid[0][0] % x
        for r in range(R):
            for c in range(C):
                if (grid[r][c] % x) != is_possible:
                    return -1
                nums.append(grid[r][c])
        nums.sort()
        N = len(nums)
        
        if N == 1:
            return 0

        median = nums[N // 2 - 1] 

        def go(median):
            res = 0
            for i in range(N):
                res += abs(nums[i] - median) // x
            return res

        return min(go(nums[N // 2 - 1]), go(nums[N // 2]))