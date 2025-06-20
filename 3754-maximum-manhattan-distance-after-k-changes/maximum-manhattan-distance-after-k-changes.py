class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        f = collections.Counter()

        res = 0
        for d in s:
            f[d] += 1
            x, y = 0, 0
            used = 0
            if f['N'] > f['S']:
                used = min(k, f['S'])
                x = f['N'] - f['S'] + (used * 2)
            else:
                used = min(k, f['N'])
                x = f['S'] - f['N'] + (used * 2)
            if f['E'] > f['W']:
                used = min(k - used, f['W'])
                y = f['E'] - f['W'] + (used * 2)
            else:
                used = min(k - used, f['E'])
                y = f['W'] - f['E'] + (used * 2)
            res = max(res, x + y)
            
        return res