class Solution:
    def maximumScore(self, nums: List[int], s: str) -> int:
        pq = []
        res = 0
        N = len(nums)
        for i in range(N):
            heappush(pq, -nums[i])
            if s[i] == '1':
                if pq:
                    res += -heappop(pq)
        return res