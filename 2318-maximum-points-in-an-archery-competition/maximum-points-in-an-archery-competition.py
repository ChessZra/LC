class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        INF = 10 ** 20

        def solve(arrows_left, index):
            if index < 0:
                if arrows_left < 0:
                    return -INF, tuple()
                else:
                    return 0, tuple()

            take, path_take = solve(arrows_left - (aliceArrows[index] + 1), index - 1)
            dont, path_dont = solve(arrows_left, index - 1)

            path_take = list(path_take)
            path_take.append(index)
            take += index

            if take >= dont:
                return take, tuple(path_take)
            
            return dont, path_dont

        res = [0] * 12
        _, arr = solve(numArrows, 11)

        for index in arr:
            res[index] = aliceArrows[index] + 1

        sm = sum(res)
        if sm < numArrows:
            res[0] += numArrows - sm
        return res