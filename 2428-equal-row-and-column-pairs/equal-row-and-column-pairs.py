class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        N = len(grid)
        R = collections.Counter()
        C = collections.Counter()
        for r in range(N):
            R[tuple(grid[r])] += 1
        
        for c in range(N):
            tup = []
            for r in range(N):
                tup.append(grid[r][c])
            C[tuple(tup)] += 1

        res = 0
        for tup, freq in R.items():
            res += R[tup] * C[tup]
        return res