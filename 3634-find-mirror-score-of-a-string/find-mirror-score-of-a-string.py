class Solution:
    def calculateScore(self, s: str) -> int:
        f = defaultdict(list)
        res = 0
        N = len(s)
        ord_a = ord('a')
        ord_z = ord('z')
        for i in range(N):
            mirror = chr(ord_a + (ord_z - ord_a) - (ord(s[i]) - ord_a))
            if f[mirror]:
                res += i - f[mirror].pop()
            else:
                f[s[i]].append(i)
        return res
