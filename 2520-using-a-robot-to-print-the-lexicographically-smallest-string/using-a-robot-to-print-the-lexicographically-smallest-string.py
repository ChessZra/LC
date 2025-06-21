class Solution:
    def robotWithString(self, s: str) -> str:
        N = len(s)

        suffix = [None] * N
        mn = 10 ** 20
        for i in range(N - 1, -1, -1):
            suffix[i] = mn
            mn = min(mn, ord(s[i]))
        
        res = ''
        stk = []
        for i in range(N):
            stk.append(s[i])

            while stk and ord(stk[-1]) <= suffix[i]:
                res += stk.pop()

        return res