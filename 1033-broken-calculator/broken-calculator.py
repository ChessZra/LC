class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        best = 10 ** 20

        def dfs(cur, count):
            if cur <= startValue:
                nonlocal best
                best = min(best, count + startValue - cur)
            if cur == 1:
                return
            if cur % 2 == 1:
                dfs(cur + 1, count + 1)
            else:
                dfs(cur // 2, count + 1)
        dfs(target, 0)
        return best