class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        # Bishop directions
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        row, col = c, d
        for dr, dc in directions:
            nr, nc = row + dr, col + dc  
            while 1 <= nr <= 8 and 1 <= nc <= 8:
                if nr == a and nc == b:
                    break
                if nr == e and nc == f:
                    return 1
                nr, nc = nr + dr, nc + dc
        # Rook directions
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        row, col = a, b
        for dr, dc in directions:
            nr, nc = row + dr, col + dc  
            while 1 <= nr <= 8 and 1 <= nc <= 8:
                if nr == c and nc == d:
                    break
                if nr == e and nc == f:
                    return 1
                nr, nc = nr + dr, nc + dc

        return 2
