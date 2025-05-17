class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        res = 0
        cols_suffix = [[0] * C for _ in range(R)]
        cols_prefix = [[0] * C for _ in range(R)]

        rows_suffix = [[0] * C for _ in range(R)]
        rows_prefix = [[0] * C for _ in range(R)]

        for r in range(R):
            count = 0
            for c in range(C - 1, -1, -1):
                cols_suffix[r][c] = count
                if grid[r][c] == 1:
                    count += 1

            count = 0
            for c in range(C):
                cols_prefix[r][c] = count
                if grid[r][c] == 1:
                    count += 1

        for c in range(C):
            count = 0
            for r in range(R - 1, -1, -1):
                rows_suffix[r][c] = count
                if grid[r][c] == 1:
                    count += 1
            
            count = 0
            for r in range(R):
                rows_prefix[r][c] = count
                if grid[r][c] == 1:
                    count += 1

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    res += rows_suffix[r][c] * cols_suffix[r][c]
                    res += rows_suffix[r][c] * cols_prefix[r][c]
                    res += rows_prefix[r][c] * cols_suffix[r][c]
                    res += rows_prefix[r][c] * cols_prefix[r][c]

        return res