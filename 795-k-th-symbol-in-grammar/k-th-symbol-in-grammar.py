class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        def solve(n, k, cur):
            if n == 1:
                # 0-indexed
                return 1 if cur == 0 else 0
            
            if k % 2 == 0:
                return solve(n - 1, k // 2, cur)
            else:
                return solve(n - 1, (k - 1) // 2, 1 - cur) 

        if solve(n, k - 1, 1):
            return 1

        return 0