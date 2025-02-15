import math

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        
        """
        x is our random integer
        good if <= x has at least n ugly
        union formula btww thx for stats <3
        - A union B union C
        - = A + B + C - (A union B) - (A union C) - (B union C) + (A union B + union C)
        """
        def good(x):
            count = (x // a) + (x // b) + (x // c)
            count -= x // math.lcm(a, b)
            count -= x // math.lcm(a, c)
            count -= x // math.lcm(b, c)
            count += x // math.lcm(a, b, c)
            return count >= n

        l, r = 0, 10 ** 20
        while l < r:
            m = (l + r) // 2

            if good(m):
                r = m
            else:
                l = m + 1

        return l