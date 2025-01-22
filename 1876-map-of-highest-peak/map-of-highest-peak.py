class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        R, C = len(isWater), len(isWater[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        res = [[None] * C for _ in range(R)]
        
        q = deque([])
        for r in range(R):
            for c in range(C):
                if isWater[r][c] == 1:
                    res[r][c] = 0
                    q.append((r, c))

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < R and 0 <= nc < C and res[nr][nc] is None:
                    res[nr][nc] = res[r][c] + 1
                    q.append((nr, nc))

        return res