class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balls = {}
        res = []
        running = 0
        colors = collections.Counter()
        for ball, color in queries:
            if ball not in balls:
                balls[ball] = color
                if colors[color] == 0:
                    running += 1
                colors[color] += 1
            else:
                colors[balls[ball]] -= 1
                if colors[balls[ball]] == 0:
                    running -= 1
                balls[ball] = color
                if colors[color] == 0:
                    running += 1
                colors[color] += 1
            res.append(running)
        return res