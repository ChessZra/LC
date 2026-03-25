class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        def rotate(matrix):
            R, C = len(matrix), len(matrix[0])
            new_matrix = [[None] * R for _ in range(C)]
            for r in range(R):
                for c in range(C):
                    new_matrix[c][r] = matrix[r][c]
            return new_matrix
        def solve(matrix):
            R, C = len(matrix), len(matrix[0])
            if R == 1: 
                return False
            arr = [[0] * C for _ in range(R)]
            for r in range(R - 1, -1, -1):
                running_sum = 0
                for c in range(C - 1, -1, -1):
                    running_sum += matrix[r][c]
                    if r < R - 1:
                        arr[r][c] = running_sum + arr[r + 1][c]
                    else:
                        arr[r][c] = running_sum            
            first, last = {}, {}
            for r in range(R):
                for c in range(C):
                    if matrix[r][c] not in first:
                        first[matrix[r][c]] = (r, c)
                    last[matrix[r][c]] = (r, c)
            for r in range(1, R):
                first_section = arr[0][0] - arr[r][0]
                second_section = arr[r][0]
                if first_section == second_section:
                    return True
            return False
        hor = solve(grid)
        if not hor:
            return solve(rotate(grid))
        return hor

