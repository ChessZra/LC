class Solution:
    def smallestPalindrome(self, s: str) -> str:
        N = len(s)
        f = collections.Counter(s)
        res = ''
        middle = None
        while True:
            flag = False

            for i in range(26):
                c = chr(ord('a') + i)
                if f[c] >= 2 and not flag:
                    flag = True
                    res += c
                    f[c] -= 2
                elif f[c] == 1:
                    middle = c

            if not flag:
                break
        if middle is None:
            return res + res[::-1]
        return res + middle + res[::-1]