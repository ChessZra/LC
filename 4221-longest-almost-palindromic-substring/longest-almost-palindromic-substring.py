class Solution:
    def almostPalindromic(self, s: str) -> int:
        N = len(s)
        def solve(left, right, used):
            if left < 0 or right >= N:
                return int(not used and (right < N or left >= 0))
            if s[left] != s[right]:
                if used:
                    return 0
                else:
                    return 1 + max(solve(left - 1, right, True), 
                            solve(left, right + 1, True))
            return (2 if left != right else 1) + solve(left - 1, right + 1, used)
        res = 0
        for i in range(N):
            res = max(res, solve(i, i, False))
            if i < N - 1:
                res = max(res, solve(i, i + 1, False))
        return res