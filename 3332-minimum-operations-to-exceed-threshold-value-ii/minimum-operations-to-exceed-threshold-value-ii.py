class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        pq = []
        for num in nums:
            heappush(pq, num)

        res = 0

        while len(pq) >= 2:
            a = heappop(pq)
            b = heappop(pq)

            if min(a, b) >= k:
                return res

            heappush(pq, min(a, b) * 2 + max(a, b))

            res += 1
        
        # answer is guaranteed
        return res
