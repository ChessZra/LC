class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        pq = []
        res = []
        for x, y in queries:

            heappush(pq, -(abs(x) + abs(y)))

            if len(pq) > k:
                heappop(pq)

            if len(pq) == k:
                res.append(-pq[0])
            else:
                res.append(-1)
        
        return res