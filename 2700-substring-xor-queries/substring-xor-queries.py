class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        vals = defaultdict(list)
        for i, q in enumerate(queries):
            vals[q[0] ^ q[1]].append(i)
        mp = {}
        for i in range(len(s)):
            current = 0
            for j in range(i, len(s)):
                if j - i + 1 > 32:
                    break
                current = current << 1
                current |= int(s[j])
                if current in vals:
                    if current in mp:
                        if mp[current][1] - mp[current][0] > (j - i):
                            mp[current] = [i, j]
                        continue
                    mp[current] = [i, j]
        res = [None] * len(queries)
        for k, v in vals.items():
            for i in v:
                res[i] = mp.get(k, [-1, -1])
        return res