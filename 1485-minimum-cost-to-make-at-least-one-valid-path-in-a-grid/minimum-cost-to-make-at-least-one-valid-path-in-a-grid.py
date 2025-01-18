class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        pq = [(0, 0, 0)]
        visited = set()
        while pq:
            cost, r, c = heappop(pq)

            if r == R - 1 and c == C - 1:
                return cost

            if (r, c) in visited or (r < 0 or r >= R or c < 0 or c >= C):
                continue
            visited.add((r, c))

            # right
            heappush(pq, (cost + int(grid[r][c] != 1), r, c + 1))
            # left
            heappush(pq, (cost + int(grid[r][c] != 2), r, c - 1))
            # down 
            heappush(pq, (cost + int(grid[r][c] != 3), r + 1, c))
            # up
            heappush(pq, (cost + int(grid[r][c] != 4), r - 1, c))


        return -1
