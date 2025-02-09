class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        ranges.sort()
        MOD = 10 ** 9 + 7
        N = len(ranges)

        if N == 1:
            return 2

        # print(ranges)
        res = 1
        streak = 2
        mx = ranges[0][1]
        for i in range(1, N):
            if ranges[i][0] <= mx:
                pass
            else:
                streak *= 2
                streak %= MOD
            mx = max(mx, ranges[i][1])

        return streak