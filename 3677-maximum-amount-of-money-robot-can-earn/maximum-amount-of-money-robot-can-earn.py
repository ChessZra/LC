class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        R, C = len(coins), len(coins[0])
        directions = [(0, 1), (1, 0)]
        INF = 10 ** 20
        @cache
        def solve(r, c, used):
            if r == R - 1 and c == C - 1:
                if coins[r][c] < 0 and used < 2:
                    return 0
                return coins[r][c]

            best = -INF
            if used < 2:
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < R and 0 <= nc < C:
                        if coins[r][c] < 0:
                            best = max(best, solve(nr, nc, used + 1))
                        best = max(best, coins[r][c] + solve(nr, nc, used))
            else:
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < R and 0 <= nc < C:
                        best = max(best, coins[r][c] + solve(nr, nc, used))
            return best
        
        return solve(0, 0, 0)
