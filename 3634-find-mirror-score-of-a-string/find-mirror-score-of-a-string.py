class Solution:
    def calculateScore(self, s: str) -> int:
        f = defaultdict(list)
        res = 0
        N = len(s)
        delta = ord('a') + ord('z')
        for i in range(N):
            mirror = chr(delta - ord(s[i]))
            if f[mirror]:
                res += i - f[mirror].pop()
            else:
                f[s[i]].append(i)
        return res
