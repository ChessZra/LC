class Solution:
    def lastRemaining(self, n: int) -> int:
        """
        1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
        2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30
        4, 8, 12, 16, 20, 24, 28        
        8, 16, 24

        dx = 1
        l = 1
        r = n
        1 2 3 4 5 6 7 8 9

        // dx = 2
        // l += dx
        // r -= dx
        dx = 2
        l = 2
        r = 8
        2, 4, 6, 8

        // dx = 4
        // l = stays the same because of even number of elements.
        // r -= dx
        dx = 4
        l = 2
        r = 6
        """
        dx = 1
        l, r = 1, n
        left = True
        i = 0
        while l != r:
            dx = 2 ** i
            if left:
                if ((r - l) // dx + 1) % 2 == 1:
                    r -= dx
                l += dx
            else:
                if ((r - l) // dx + 1) % 2 == 1:
                    l += dx
                r -= dx
            i += 1
            left = not left
        return l
            