class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        INF = 10 ** 20
        def go(x):
            # test if equal to targetSeconds
            temp = '0' * (4 - len(x)) + x
            x_to_seconds = (int(temp[:-2]) * 60 + int(temp[-2:]))
            if x_to_seconds != targetSeconds:
                return INF

            cur = str(startAt)
            total_moves_cost = 0
            for char in x:
                if char != cur:
                    total_moves_cost += moveCost
                cur = char
            total_push_cost = len(x) * pushCost

            return total_push_cost + total_moves_cost
        
        best = INF
        for x in range(1, 10000):
            best = min(best, go(str(x)))
        return best