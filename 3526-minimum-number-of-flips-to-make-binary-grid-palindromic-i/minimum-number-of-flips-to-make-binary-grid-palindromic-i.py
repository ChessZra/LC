class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        
        R, C = len(grid), len(grid[0])

        case1 = 0
        for r in range(R):
            for c in range(C // 2):
                if grid[r][c] != grid[r][C - 1 - c]:
                    case1 += 1
        
        case2 = 0
        for c in range(C):
            for r in range(R // 2):
                if grid[r][c] != grid[R - 1 - r][c]:
                    case2 += 1
        
        return min(case1, case2)