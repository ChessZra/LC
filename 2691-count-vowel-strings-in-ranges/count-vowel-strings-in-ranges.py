class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = ['a', 'e', 'i', 'o', 'u']
        rs = 0
        prefix = []
        for w in words:
            if w[0] in vowels and w[-1] in vowels:
                rs += 1
            prefix.append(rs)
        
        res = []
        for l, r in queries:
            res.append(prefix[r] - (0 if l == 0 else prefix[l - 1]))
        return res