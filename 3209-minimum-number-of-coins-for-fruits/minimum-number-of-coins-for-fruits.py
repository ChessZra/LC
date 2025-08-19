class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        N = len(prices)
        @cache
        def solve(index):
            if index >= N:
                return 0
            best = 10 ** 20
            for i in range(index + 1, index + index + 2):
                best = min(best, solve(i + 1), solve(i))
            return best + prices[index]
        return solve(0)