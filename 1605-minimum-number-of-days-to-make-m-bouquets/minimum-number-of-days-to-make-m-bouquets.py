class Solution:
    def minDays(self, bloomDay: List[int], M: int, k: int) -> int:
        N = len(bloomDay)
        def good(x):
            count = 0
            res = 0
            for i in range(N):
                if x >= bloomDay[i]:
                    count += 1
                else:
                    count = 0
                
                if count == k:
                    count = 0
                    res += 1
            return res >= M

        l, r = 0, max(bloomDay)
        while l < r:
            m = (l + r) // 2
            if good(m):
                r = m
            else:
                l = m + 1
        return l if good(l) else -1