class Solution:
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:
        N = len(s)

        def prv(c):
            return chr(((ord(c) - ord("a") - 1) % 26) + ord("a"))

        def nxt(c):
            return chr(((ord(c) - ord("a") + 1) % 26) + ord("a"))

        @cache
        def solve(left, right, k):
            if left == right:
                return 1
            elif left > right:
                return 0

            best = 0
            if s[left] == s[right]:
                best = max(best, 2 + solve(left + 1, right - 1, k))
            else: # how many ops to convert s[left] -> s[right]? 
                # forwards
                t1 = (ord(s[right]) - ord(s[left])) % 26
                t2 = 26 - t1
                if k >= min(t1, t2):
                    best = max(best, 2 + solve(left + 1, right - 1, k - min(t1, t2)))

                # do nothing
                best = max(best, max(solve(left + 1, right, k), solve(left, right - 1, k), solve(left + 1, right - 1, k)))
            return best

        return solve(0, N - 1, k)

