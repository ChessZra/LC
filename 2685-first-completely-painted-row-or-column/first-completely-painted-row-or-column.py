class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        R, C = len(mat), len(mat[0])

        rows = [C] * R
        cols = [R] * C

        rf = {}
        cf = {}
        for r in range(R):
            for c in range(C):
                rf[mat[r][c]] = r
                cf[mat[r][c]] = c

        for index, num in enumerate(arr):
            rows[rf[num]] -= 1
            cols[cf[num]] -= 1
            if rows[rf[num]] == 0 or cols[cf[num]] == 0:
                return index

        return 0