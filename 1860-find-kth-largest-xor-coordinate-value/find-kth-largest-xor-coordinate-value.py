class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        R, C = len(matrix), len(matrix[0])
        pq = [] # min heap of size k

        dp = [[0] * (C + 1) for _ in range(R + 1)]
        for r in range(R):
            rx = 0
            for c in range(C):
                rx ^= matrix[r][c]
                dp[r + 1][c + 1] = rx ^ dp[r][c + 1]
                heappush(pq, dp[r + 1][c + 1])
                if len(pq) > k:
                    heappop(pq)

        return pq[0]