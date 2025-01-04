class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        N2 = len(b)
        N1 = len(a)
        INF = float('inf')

        @cache
        def solve(index1, index2):
            if index1 >= N1:
                return 0
            if index2 >= N2:
                return -INF
            
            best = -INF
            # take
            best = max(best, (a[index1] * b[index2]) + solve(index1 + 1, index2 + 1))
            # dont take
            best = max(best, solve(index1, index2 + 1))
            return best

        return solve(0, 0)