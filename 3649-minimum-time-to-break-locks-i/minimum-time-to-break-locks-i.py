class Solution:
    def findMinimumTime(self, strength: List[int], k: int) -> int:
        N = len(strength)
        target = 2 ** N - 1

        @cache
        def solve(bitmask, x):
            if bitmask == target:
                return 0
            
            best = 10 ** 20
            for i in range(N):
                if bitmask & (1 << i) == 0:
                    t = math.ceil(strength[i] / x) 
                    best = min(best, t + solve(bitmask | (1 << i), x + k))
            return best
        
        return solve(0, 1)