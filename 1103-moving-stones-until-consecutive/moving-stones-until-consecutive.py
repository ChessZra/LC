class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
    
        def mn(a, b, c):
            a, b, c = sorted([a, b, c])

            if b - a == 2 or c - b == 2:
                return 1
            res = 0
            if b - a != 1:
                res += 1
            if c - b != 1:
                res += 1
            return res

        INF = float('inf')
        @cache
        def mx(a, b, c):
            st = sorted([a, b, c])
        
            # overlapping base case, invalid
            if st[1] == st[0] or st[1] == st[2]:
                return -INF
            # consecutive base case
            if (st[1] - st[0]) == 1 and (st[2] - st[1]) == 1:
                return 0

            best = -INF
            # move lowest x
            if a < b and a < c:
                best = max(best, mx(a + 1, b, c) + 1)
            elif b < a and b < c:
                best = max(best, mx(a, b + 1, c) + 1) 
            elif c < a and c < b:
                best = max(best, mx(a, b, c + 1) + 1)
                
            # move highest x
            if a > b and a > c:
                best = max(best, mx(a - 1, b, c) + 1) 
            elif b > a and b > c:
                best = max(best, mx(a, b - 1, c) + 1) 
            elif c > a and c > b:
                best = max(best, mx(a, b, c - 1) + 1) 
            return best
        
        return [mn(a, b, c), mx(a, b, c)]

        # 1 3 5