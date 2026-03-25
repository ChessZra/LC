class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        def rotate(matrix):
            R, C = len(matrix), len(matrix[0])
            new_matrix = [[None] * R for _ in range(C)]
            for r in range(R):
                for c in range(C):
                    new_matrix[c][r] = matrix[r][c]
            return new_matrix
        def out_of_bounds(r, c, top_bound, lower_bound, C):
            if ((r + 1) >= lower_bound and (r - 1) <= top_bound) and not (c == 0 or c == C - 1):
                return True
            if ((c + 1) >= C and (c - 1) < 0) and not (r == top_bound + 1 or r == lower_bound - 1):
                return True
            return False
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
                if first_section < second_section: # remove something from section 2
                    delta = second_section - first_section
                    if delta in last and last[delta][0] >= r and not out_of_bounds(last[delta][0], last[delta][1], r - 1, R, C):
                        return True
                else: # remove something from section 1
                    delta = first_section - second_section
                    if delta in first and first[delta][0] < r and not out_of_bounds(first[delta][0], first[delta][1], -1, r, C):
                        return True
            return False
        hor = solve(grid)
        if not hor:
            return solve(rotate(grid))
        return hor

