class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        while True:
            changed = False
            # try to flip all the rows
            for r in range(R):
                if grid[r][0] == 0:
                    for c in range(C):
                        grid[r][c] = 1 - grid[r][c]
                    changed = True

            # try to flip all the cols
            for c in range(C):
                z = 0
                for r in range(R):
                    if grid[r][c] == 0:
                        z += 1
                
                if z > (R - z):
                    for r in range(R):
                        grid[r][c] = 1 - grid[r][c]
                        changed = True
                
            if not changed:
                break
                
        res = 0
        for r in range(R):
            i = 0
            for c in range(C - 1, -1, -1):
                if grid[r][c] == 1:
                    res += (2 ** i)
                i += 1
        return res  
