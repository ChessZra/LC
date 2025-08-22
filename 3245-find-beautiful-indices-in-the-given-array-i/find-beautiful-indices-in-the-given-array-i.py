class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        N = len(s)
        match = []
        for i in range(N):
            if b == s[i:i+len(b)]:
                match.append(i)
        res = []
        for i in range(N):
            if a == s[i:i+len(a)]:
                l, r = 0, len(match) - 1
                while l < r:
                    m = (l + r) // 2
                    if match[m] >= i:
                        r = m
                    else:
                        l = m + 1
                if l >= 0 and l < len(match):
                    if abs(i - match[l]) <= k or (l < len(match) - 1 and abs(i - match[l + 1]) <= k) or (l > 0 and abs(i - match[l - 1] <= k)):
                        res.append(i)
        return res