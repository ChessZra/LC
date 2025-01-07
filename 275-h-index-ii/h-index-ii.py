class Solution:
    def hIndex(self, citations: List[int]) -> int:
        N = len(citations)

        def good(h):
            return citations[-h] >= h

        l, r = 0, N
        while l < r:
            m = (l + r + 1) // 2

            if good(m):
                l = m 
            else:
                r = m - 1

        return l