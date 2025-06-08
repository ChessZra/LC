class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        # this is like a heatmap
        r = R - 1
        c = 0
        res = 0

        while r >= 0:

            while c < C and grid[r][c] >= 0:
                c += 1    

            if c >= C:
                break

            res += C - c
            r -= 1

        return res