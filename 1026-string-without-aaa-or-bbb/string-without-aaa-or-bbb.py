class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        
        @cache
        def solve(a, b, last):
            if a == 0 and b == 0:
                return ""
            if a < 0 or b < 0:
                return None

            if solve(a - 1, b, 0) is not None and last != 0:                
                return "a" + solve(a - 1, b, 0)

            if solve(a - 2, b, 0) is not None and last != 0:
                return "aa" + solve(a - 2, b, 0)
            
            if solve(a, b - 1, 1) is not None and last != 1:
                return "b" + solve(a, b - 1, 1)

            if solve(a, b - 2, 1) is not None and last != 1:
                return "bb" + solve(a, b - 2, 1)
            
            return None

        return solve(a, b, -1)