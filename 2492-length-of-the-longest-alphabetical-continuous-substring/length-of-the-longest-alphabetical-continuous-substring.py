class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        N = len(s)

        best = 1
        streak = 1
        for i in range(1, N):
            if (ord(s[i]) - ord(s[i - 1])) == 1:
                streak += 1
            else:
                streak = 1
            best = max(best, streak)
        return best