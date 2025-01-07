class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = collections.defaultdict(list)
        for row, seat in reservedSeats:
            rows[row].append(seat)

        res = 0
        for row, taken_seats in rows.items():

            a, b, c = 0, 0, 0
            if 2 not in taken_seats and 3 not in taken_seats and 4 not in taken_seats and 5 not in taken_seats:
                a += 1
            if 6 not in taken_seats and 7 not in taken_seats and 8 not in taken_seats and 9 not in taken_seats:
                b += 1
                  
            if a == 0 and b == 0:
                if 4 not in taken_seats and 5 not in taken_seats and 6 not in taken_seats and 7 not in taken_seats:
                    c += 1        
    
            res += a + b + c

            n -= 1
        
        return res + (n * 2)