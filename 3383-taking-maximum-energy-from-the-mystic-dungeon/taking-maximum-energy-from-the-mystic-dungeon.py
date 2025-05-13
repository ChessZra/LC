class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        INF = 10 ** 20
        N = len(energy)
        @cache
        def solve(index):
            if index >= N:
                return 0
            return energy[index] + solve(index + k)
        
        best = -INF
        for i in range(N):
            best = max(best, solve(i))
        return best