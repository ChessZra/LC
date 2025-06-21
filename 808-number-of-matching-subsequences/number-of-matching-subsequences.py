class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        f = collections.defaultdict(list)

        for i in range(len(s)):
            f[s[i]].append(i)

        res = 0
        for word in words:
            last_word = -1
            can = True
            for c in word:
                arr = f[c]
                l, r = 0, len(arr) - 1
                while l < r:
                    m = (l + r) // 2
                    if arr[m] > last_word:
                        r = m
                    else:
                        l = m + 1
                if r >= 0 and arr[r] > last_word:
                    last_word = arr[r]
                else:
                    can = False
            if can:
                res += 1
        return res