class Solution:
    def maximumXor(self, s: str, t: str) -> str:
        N = len(s)
        ones = t.count('1')
        zeroes = N - ones
        res = ''
        for i in range(N):
            if s[i] == '1':
                if zeroes:
                    res += '1'
                    zeroes -= 1
                elif ones:
                    res += '0'
                    ones -= 1
            else:
                if ones:
                    res += '1'
                    ones -= 1
                else:
                    res += '0'
                    zeroes -= 1
        return res
