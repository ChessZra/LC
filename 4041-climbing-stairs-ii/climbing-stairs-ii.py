class Solution:
    def climbStairs(self, N: int, costs: List[int]) -> int:
        INF = 10 ** 20
        @cache
        def solve(index):
            if index == N - 1:
                return 0
            best = INF
            if index + 1 < N:
                best = min(best, solve(index + 1) + costs[index + 1] + (index + 1 - index) ** 2)
            if index + 2 < N:
                best = min(best, solve(index + 2) + costs[index + 2] + (index + 2 - index) ** 2)
            if index + 3 < N:
                best = min(best, solve(index + 3) + costs[index + 3] + (index + 3 - index) ** 2)
            return best
        return solve(-1)