class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        N = len(rungs)
        res = 0
        cur = 0
        for index in range(N):
            if rungs[index] > (cur + dist):
                d = rungs[index] - cur
                res += d // dist
                if d % dist == 0:
                    res -= 1 # exclude last rung
            
            cur = rungs[index]
        return res